from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    # birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError('This email exists ')
        return email
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)
