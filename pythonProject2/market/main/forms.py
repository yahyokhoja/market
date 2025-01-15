from .models import Task
from django.forms import ModelForm,TextInput,Textarea


class Taskform(ModelForm):
    class Meta:
        model = Task
        fields = ["nom","harid","furush"]
        widgets = {
            "nom":TextInput(attrs={
                'class':'form-control',
                'placeholder': 'ном'
            }),
            "harid": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'харид'
            }),
            "furush": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'фуруш'
            }),
        }
