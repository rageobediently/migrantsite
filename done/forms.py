from django import forms


class checkdate(forms.Form):
    number = forms.IntegerField(help_text="Введите номер заказа")