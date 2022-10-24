from django.forms import ModelForm, Textarea, TextInput
from .models import Order


class OrderCreateForm(ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'clients_number', 'city', 'message')

        widgets = {
                'first_name': TextInput(attrs={'placeholder': "Ваше ім'я", 'cols': 35, 'rows': 1}, ),
                'last_name': TextInput(attrs={'placeholder': 'Ваше прізвище', 'cols': 35, 'rows': 1}, ),
                'clients_number': TextInput(attrs={'placeholder': 'Ваш номер телефону', 'cols': 35, 'rows': 1}, ),
                'city': TextInput(attrs={'placeholder': 'Місто', 'cols': 35, 'rows': 1}, ),
                'message': Textarea(attrs={'placeholder': 'Коментар до замовлення', 'cols': 55, 'rows': 5}, ),

            }