import os
from django.shortcuts import render, redirect
from PyPDF2 import PdfMerger
from django.conf import settings
from unirpdf.forms import UploadPDFsForm
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from urllib.parse import quote_plus
from urllib.parse import unquote_plus
from .models import Report
from datetime import datetime

from django.core.files import File

def verificar_pdf(request):
    pdf_url = request.session.get('pdf_url', '')
    pdf_name = 'unirpdf/' + pdf_url.split('/')[-1] # 'unirpdf/' es agregado al inicio
    pdf_name_encoded = quote_plus(pdf_name)
    
    if request.method == 'POST':
        # Aquí obtenemos la información de la sucursal y el periodo de la sesión.
        sucursal = request.session.get('sucursal')
        periodo = request.session.get('periodo')

        # Abre el archivo en modo lectura binaria
        with open(os.path.join(settings.MEDIA_ROOT, pdf_name), 'rb') as pdf_file:
            # Crea un nuevo registro en la base de datos con la información recibida.
            Report.objects.create(
                sucursal=sucursal,
                periodo=periodo,
                user=request.user,
                file=File(pdf_file, pdf_name),  # Aquí estamos pasando el nombre del archivo como segundo argumento
            )
        
        # Redirige a la página de descarga del archivo.
        return redirect('buscar_reportes')

    return render(request, 'unirpdf/verificar.html', {'pdf_url': pdf_url, 'pdf_name': pdf_name_encoded})

def cargar_pdfs(request):
    if request.method == 'POST':
        form = UploadPDFsForm(request.POST, request.FILES)
        if form.is_valid():
            merger = PdfMerger()

            # Crea una carátula
            cover_path = os.path.join(settings.STATIC_ROOT, 'unirpdf', 'cover.pdf')
            create_cover(cover_path, form.cleaned_data['sucursal'], form.cleaned_data['periodo'], request.user)

            # Agrega la carátula al principio
            merger.append(cover_path)

            for key, value in form.cleaned_data.items():
                if key.startswith("pdf"):
                    merger.append(value)

            # Concatena Sucursal y Periodo para formar el nombre del archivo
            filename = f"{form.cleaned_data['sucursal']}_{form.cleaned_data['periodo']}.pdf"
            output_filename = os.path.join(settings.MEDIA_ROOT, 'unirpdf', filename)

            with open(output_filename, 'wb') as output_pdf:
                merger.write(output_pdf)

            pdf_url = f"{settings.MEDIA_URL}unirpdf/{filename}"

            # Almacena el pdf_url en la sesión
            request.session['pdf_url'] = pdf_url
            # Almacena la sucursal y el periodo en la sesión
            request.session['sucursal'] = form.cleaned_data['sucursal']
            request.session['periodo'] = form.cleaned_data['periodo']
            request.session['filename'] = filename

            # Redirige a la vista de verificación
            return redirect('verificar_pdf')
    else:
        form = UploadPDFsForm()

    return render(request, 'unirpdf/cargar.html', {'form': form})


def cancelar_pdf(request, path):
    path_decoded = unquote_plus(path)
    pdf_file = os.path.join(settings.MEDIA_ROOT, path_decoded)
    if os.path.exists(pdf_file):
        os.remove(pdf_file)
    return redirect('cargar_pdf')

def create_cover(path, sucursal, periodo, user):
    c = canvas.Canvas(path, pagesize=A4)
    width, height = A4

    # Agregar el logo
    logo_path = os.path.join(settings.STATIC_ROOT, 'sitio', 'logo_empresa.png')
    c.drawImage(logo_path, width / 2 - 50, height - 150, width=100, height=100)  # ajusta las dimensiones según tus necesidades

    c.setFont("Helvetica", 24)
    c.drawCentredString(width / 2, height / 2 + 4*cm, f"Reporte de movimiento diario de la Sucursal")
    c.setFont("Helvetica", 18)
    c.drawCentredString(width / 2, height / 2 + 2*cm, f"Periodo del reporte: {sucursal}")
    c.setFont("Helvetica", 18)
    c.drawCentredString(width / 2, height / 2, f"{periodo}")
    c.setFont("Helvetica", 16)
    c.drawCentredString(width / 2, height / 2 - 2*cm, f"Responsable: {user.first_name} {user.last_name}")

    # Dibujar el año actual en la parte inferior de la página
    current_year = datetime.today().year
    c.setFont("Helvetica", 24)  # Ajusta el tamaño del texto
    c.setFillColorRGB(0.5, 0.5, 0.5)  # Establece el color del texto a gris
    c.drawCentredString(width / 2, 2*cm, str(current_year))

    c.showPage()
    c.save()

def consultar(request):
    reports = Report.objects.all()  # Recuperar todos los registros de la tabla Report
    return render(request, 'unirpdf/consultar.html', {'reports': reports})

def buscar_reportes(request):
    if request.method == 'POST':
        buscar = request.POST.get('buscar')
        # Aquí puedes implementar la lógica para buscar en los reportes.
        # Por ejemplo, si 'buscar' es el nombre de la sucursal:
        reports = Report.objects.filter(sucursal__icontains=buscar)
    else:
        reports = Report.objects.all()
    return render(request, 'unirpdf/consultar.html', {'reports': reports})
