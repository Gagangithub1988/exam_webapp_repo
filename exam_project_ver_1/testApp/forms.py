from django import forms
from .models import Account
from django.contrib.auth.forms import PasswordResetForm
class AccountForm(forms.ModelForm):
    class Meta:
        model=Account
        fields=['first_name','last_name','email','contact_number','profile_pic']
        
class EmailValidationOnForgotPassword(PasswordResetForm):

    def clean_email(self):
        email = self.cleaned_data['email']
        if not Account.objects.filter(email__iexact=email, is_active=True).exists():
            msg = ("There is no user registered with the specified E-Mail address.")
            self.add_error('email', msg)
        return email
