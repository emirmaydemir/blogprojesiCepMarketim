from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
import re
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
class LoginForm(forms.Form):
    username=forms.CharField(max_length=100,label='Kullanıcı Adı')
    password=forms.CharField(max_length=100,label='Parola',widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Kullanıcı adınızı veya şifrenizi yanlış girdiniz!")
        return super(LoginForm, self).clean()


class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=100, label='Kullanıcı Adı')
    password1 = forms.CharField(max_length=100, label='Parola', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100, label='Parola Doğrulama', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
                'username',
                'password1',
                'password2',
            ]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        username=self.cleaned_data.get("username")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Şifreler eşleşmiyor!")
        if (not re.search(regex,username)):
            raise forms.ValidationError("Mail giriniz!")
        return password2

