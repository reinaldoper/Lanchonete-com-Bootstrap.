from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Pastel, Pizza, Suco, Refrigerante, Fritas, Saladas


class PastelAdmin(ModelAdmin):
    fields = ['nome','endereço','quantidade','Tipo_Pastel','data']
    list_display = ['nome', 'endereço', 'quantidade','Tipo_Pastel', 'data']
    list_editable = ['data']


admin.site.register(Pastel, PastelAdmin)


class PizzaAdmin(ModelAdmin):
    fields = ['nome','endereço','quantidade','Tipo_Pizza','data']
    list_display = ['nome', 'endereço', 'quantidade','Tipo_Pizza', 'data']
    list_editable = ['data']


admin.site.register(Pizza, PizzaAdmin)


class SucoAdmin(ModelAdmin):
    fields = ['nome','endereço','quantidade','Tipo_Suco','data']
    list_display = ['nome', 'endereço', 'quantidade','Tipo_Suco', 'data']
    list_editable = ['data']


admin.site.register(Suco, SucoAdmin)


class RefrigeranteAdmin(ModelAdmin):
    fields = ['nome','endereço','quantidade','Tipo_Refrigerante','data']
    list_display = ['nome', 'endereço', 'quantidade','Tipo_Refrigerante', 'data']
    list_editable = ['data']


admin.site.register(Refrigerante, RefrigeranteAdmin)


class FritasAdmin(ModelAdmin):
    fields = ['nome','endereço','quantidade','Tamanho','data']
    list_display = ['nome', 'endereço', 'quantidade','Tamanho', 'data']
    list_editable = ['data']


admin.site.register(Fritas, FritasAdmin)


class SaladasAdmin(ModelAdmin):
    fields = ['nome','endereço','quantidade','Tipo_salada','data']
    list_display = ['nome', 'endereço', 'quantidade','Tipo_salada', 'data']
    list_editable = ['data']


admin.site.register(Saladas, SaladasAdmin)



# Register your models here.
