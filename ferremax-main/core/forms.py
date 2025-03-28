from django import forms
from .models import Marca,Producto,Tutorial,Ciudad,Comuna,Usuario_direccion
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Record

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = "__all__"

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"

class TutorialForm(forms.ModelForm):
    class Meta:
        model = Tutorial
        fields = "__all__"


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario_direccion
        fields = "__all__"

class ComunaForm(forms.ModelForm):
    class Meta:
        model = Comuna
        fields = "__all__"

class CiudadForm(forms.ModelForm):
    class Meta:
        model = Ciudad
        fields = "__all__"


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label = "", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Correo'}))
    first_name = forms.CharField (label = "", max_length="100", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}))
    last_name = forms.CharField (label = "", max_length="100", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Apellido'}))

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password1','password2' )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Usuario'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Requiere. 150 caracteres o menos. Letras, Digitos t @/./+/-/_ </small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Contraseña'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Tu contraseña no debe contener tu informacion personal.</li><li>Tu contraseña debe contener al menos 8 caracteres.</li><li>Tu contraseña no debe ser común.</li><li>Tu contraseña no debe contener solo numeros.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirmar Contraseña'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Ingresa tu contraseña para verificacion.</small></span>'	


class AddRecordForm(forms.ModelForm):
	first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")
	last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
	email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label="")
	phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), label="")
	address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control"}), label="")
	city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"City", "class":"form-control"}), label="")
	state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"State", "class":"form-control"}), label="")
	zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Zipcode", "class":"form-control"}), label="")

	class Meta:
		model = Record
		exclude = ("user",)
