from django import forms

class codeUploadForm(forms.Form):
    FileTitle    = forms.CharField(label='Название:', max_length=50)
    Uploadedfile = forms.FileField(label='Файл:')
    