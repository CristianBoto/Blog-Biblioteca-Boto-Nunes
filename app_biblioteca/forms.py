from cProfile import label
import email
from turtle import width
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import *
from pdb import post_mortem

class Encargado_Form(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    codigo = forms.IntegerField()
    email = forms.CharField()

class Socio_Form(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    num_socio=forms.IntegerField()
    email=forms.EmailField()
    fecha_alta=forms.DateField()

class Libro_Form(forms.Form):
    titulo = forms.CharField(max_length=50)
    autor = forms.CharField(max_length=50)
    genero = forms.CharField(max_length=50)
    codigo =forms.IntegerField()


class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    last_name= forms. CharField(label='Apellido')
    first_name= forms.CharField(label='Nombre')
    class Meta:
        model=User
        fields= ['username', 'email', 'password1', 'password2','last_name','first_name']
        help_texts= {k:"" for k in fields}



class UserEditForm(UserChangeForm):
    email= forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={'class':'form-control'}))
    last_name= forms.CharField(max_length=100,label='Apellido', widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(max_length=100,label='Nombre', widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=100,label='Usuario', widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model=User
        fields= ['username','first_name','last_name', 'email', ]
        help_texts= {k:"" for k in fields}

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(label = 'Contraseña Actual',widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password1 = forms.CharField(label = "Nueva Contraseña", widget = forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password2 =  forms.CharField(label = "Repita la contraseña" , widget = forms.PasswordInput(attrs={'class':'form-control','type':'password'}))

    class Meta:
        model = User
        fields = ["old_password","new_password1","new_password2"]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo','autor','body')
        
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'autor': forms.TextInput(attrs={'class':'form-control', 'value':'','id':'elder','type':'hidden'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        
        }   

class EditarForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo','body')
        
        widget = {
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'autor': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        
        }   

class ThreadForm(forms.Form):
  username = forms.CharField(label='', max_length=100)
  
class MessageForm(forms.Form):
  message = forms.CharField(label='', max_length=1000)