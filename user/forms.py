from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class girisForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adı")
    password = forms.CharField(label="Parola", widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(girisForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}


class kayitForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adı")
    password = forms.CharField(label="Parola", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Doğrula", widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Kullanıcı adı mevcuttur.")

        if password != password2:
            raise forms.ValidationError("Parolalar eşleşmiyor")

        values = {
            "username": username,
            "password": password
        }
        return values

    def __init__(self, *args, **kwargs):
        super(kayitForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}
