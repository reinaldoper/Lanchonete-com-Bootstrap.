from django.forms import ModelForm, forms

from .models import Pastel, Pizza, Suco, Refrigerante, Fritas, Saladas


class PastelForm(ModelForm):
    class Meta:
        model = Pastel
        fields = ['nome','endereço','quantidade','data','Tipo_Pastel']


class PizzaForm(ModelForm):
    class Meta:
        model = Pizza
        fields = ['nome','endereço','quantidade','data','Tipo_Pizza']


class SucoForm(ModelForm):
    class Meta:
        model = Suco
        fields = ['nome','endereço','quantidade','data','Tipo_Suco']


class RefrigeranteForm(ModelForm):
    class Meta:
        model = Refrigerante
        fields = ['nome','endereço','quantidade','data','Tipo_Refrigerante']


class FritasForm(ModelForm):
    class Meta:
        model = Fritas
        fields = ['nome','endereço','quantidade','data','Tamanho']


class SaladasForm(ModelForm):
    class Meta:
        model = Saladas
        fields = ['nome','endereço','quantidade','data','Tipo_salada']


