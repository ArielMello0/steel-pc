from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class BlogForm(forms.Form):
    titulo=forms.CharField(max_length=50)
    subtitulo=forms.CharField(max_length=50)
    cuerpo=forms.CharField(max_length=5000, widget = forms.Textarea)
    autor= forms.CharField(max_length=50)
    fecha= forms.DateField()
    imagen=forms.ImageField(label='imagen')

class AutorForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    email=forms.EmailField()
    profesion=forms.CharField(max_length=50)

class SuscriptorForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    email=forms.EmailField()

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    password1=forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
   

class UserEditForm(UserCreationForm):
    email=forms.EmailField()
    password1=forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
   
class AvatarForm(forms.Form):
    imagen= forms.ImageField(label="Imagen")




