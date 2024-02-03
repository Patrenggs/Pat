from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer

class CustomerCreationForm(UserCreationForm):
    name = forms.CharField(max_length=200, required=True)
    email = forms.EmailField(required=True)
    address = forms.CharField(max_length=200, required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'name', 'email', 'address']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()

        customer = Customer.objects.create(user=user, name=self.cleaned_data['name'], email=self.cleaned_data['email'], address=self.cleaned_data['address'])
        return user
