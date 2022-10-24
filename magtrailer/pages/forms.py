from django.forms import ModelForm, Textarea, TextInput
from .models import Contacts


class ContactForm(ModelForm):
    class Meta:
        model = Contacts
        fields = ('first_name', 'last_name', 'clients_number', 'message')
        widgets = {
            'message': Textarea(attrs={'placeholder': 'Задайте питання', 'cols': 45, 'rows': 12}, ),
            'first_name': TextInput(attrs={'placeholder': "Ваше ім'я"}, ),
            'last_name': TextInput(attrs={'placeholder': 'Ваше прізвище'}, ),
            'clients_number': TextInput(attrs={'placeholder': 'Номер телефону'}, )
        }
