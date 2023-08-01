from django import forms

class UploadPDFsForm(forms.Form):
    sucursal = forms.CharField(max_length=100)  # Campo de entrada para Sucursal
    periodo = forms.CharField(max_length=100)  # Campo de entrada para Periodo
    pdf1 = forms.FileField(widget=forms.FileInput(attrs={'accept':'application/pdf'}))
    pdf2 = forms.FileField(widget=forms.FileInput(attrs={'accept':'application/pdf'}))

"""     pdf3 = forms.FileField(widget=forms.FileInput(attrs={'accept':'application/pdf'}))
    pdf4 = forms.FileField(widget=forms.FileInput(attrs={'accept':'application/pdf'}))
    pdf5 = forms.FileField(widget=forms.FileInput(attrs={'accept':'application/pdf'}))
    pdf6 = forms.FileField(widget=forms.FileInput(attrs={'accept':'application/pdf'}))
    pdf7 = forms.FileField(widget=forms.FileInput(attrs={'accept':'application/pdf'}))
    pdf8 = forms.FileField(widget=forms.FileInput(attrs={'accept':'application/pdf'}))
    pdf9 = forms.FileField(widget=forms.FileInput(attrs={'accept':'application/pdf'})) 
    pdf9 = forms.FileField(widget=forms.FileInput(attrs={'accept':'application/pdf'})) 
    pdf10 = forms.FileField(widget=forms.FileInput(attrs={'accept':'application/pdf'})) """ 
