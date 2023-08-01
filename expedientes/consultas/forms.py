from django import forms
from .models import Expediente
from crispy_forms.helper import FormHelper


class ExpedienteForm(forms.ModelForm):
    class Meta:
        model = Expediente
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ExpedienteForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'input-small'
