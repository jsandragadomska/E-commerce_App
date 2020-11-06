from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class  LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )

    def clean_udername(self):
        data = self.cleaned_data.get('username')
        qs = User.objects.filter(username_iexact=data)
        if not qs.exists():
            raise forms.ValidationError("This is an invalid username.")
        return data