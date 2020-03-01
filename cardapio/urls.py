from django.urls import path

from .views import CompraPastel
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('pastel/', views.CompraPastel),
    path('pizza/',views.CompraPizza),
    path('suco/',views.CompraSuco),
    path('refrigerante/',views.CompraRefrigerante),
    path('fritas/',views.CompraFritas),
    path('saladas/',views.CompraSaladas),
    path('compras/',views.compras),
    path('compras/pasteis/', views.PastelListView.as_view(), name='pasteis'),
    path('pastel/<int:pk>/', views.PastelDetailView.as_view(), name='pastel-detail'),
    path('compras/pizzas/', views.PizzaListView.as_view(), name='pizzas'),
    path('pizza/<int:pk>/', views.PizzaDetailView.as_view(), name='pizza-detail'),
    path('compras/sucos/', views.SucoListView.as_view(), name='sucos'),
    path('suco/<int:pk>/', views.SucoDetailView.as_view(), name='suco-detail'),
    path('compras/refrigerantes/', views.RefrigeranteListView.as_view(), name='refrigerantes'),
    path('refrigerante/<int:pk>/', views.RefrigeranteDetailView.as_view(), name='refrigerante-detail'),
    path('compras/fritas/', views.FritasListView.as_view(), name='fritas'),
    path('fritas/<int:pk>/', views.FritasDetailView.as_view(), name='fritas-detail'),
    path('compras/saladas/', views.SaladasListView.as_view(), name='saladas'),
    path('saladas/<int:pk>/', views.SaladasDetailView.as_view(), name='saladas-detail'),
]