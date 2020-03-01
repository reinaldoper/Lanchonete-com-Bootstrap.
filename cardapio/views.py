from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.template.context_processors import request
from django.views import View, generic

from .models import Saladas, Fritas, Refrigerante, Pizza, Pastel, Suco
from .forms import PastelForm, PizzaForm, SucoForm, RefrigeranteForm, FritasForm, SaladasForm


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index_generic.html', context=context)


def CompraPastel(request):
    if request.method == 'POST':
        form = PastelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PastelForm()
    return render(request, 'pastel.html', {'form': form})


def CompraPizza(request):
    if request.method == 'POST':
        form = PizzaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PizzaForm()
    return render(request, 'pizza.html', {'form': form})


def CompraSuco(request):
    if request.method == 'POST':
        form = SucoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SucoForm()
    return render(request, 'suco.html', {'form': form})


def CompraRefrigerante(request):
    if request.method == 'POST':
        form = RefrigeranteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RefrigeranteForm()
    return render(request, 'refrigerantes.html', {'form': form})


def CompraFritas(request):
    if request.method == 'POST':
        form = FritasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = FritasForm()
    return render(request, 'fritas.html', {'form': form})


def CompraSaladas(request):
    if request.method == 'POST':
        form = SaladasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SaladasForm()
    return render(request, 'saladas.html', {'form': form})


def compras(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_saladas = Saladas.objects.all().count()
    num_fritas = Fritas.objects.all().count()

    # Available books (status = 'a')
    num_refrigerantes= Refrigerante.objects.all().count()
    num_pizza = Pizza.objects.all().count()
    # The 'all()' is implied by default.
    num_pastel = Pastel.objects.all().count()
    # Number of visits to this view, as counted in the session variable.
    num_suco = Suco.objects.all().count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_saladas': num_saladas,
        'num_fritas': num_fritas,
        'num_pizza': num_pizza,
        'num_refrigerantes': num_refrigerantes,
        'num_visits': num_visits,
        'num_pastel': num_pastel,
        'num_suco' : num_suco,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'compras.html', context=context)


class PastelListView(generic.ListView):
    model = Pastel
    queryset = Pastel.objects.all()
    template_name = 'lista_pastel.html'


class PastelDetailView(generic.DetailView):
    model = Pastel
    template_name = 'detalhe_pastel.html'


class PizzaListView(generic.ListView):
    model = Pizza
    queryset = Pizza.objects.all()
    template_name = 'lista_pizza.html'


class PizzaDetailView(generic.DetailView):
    model = Pizza
    template_name = 'detalhe_pizza.html'


class SucoListView(generic.ListView):
    model = Suco
    queryset = Suco.objects.all()
    template_name = 'lista_suco.html'


class SucoDetailView(generic.DetailView):
    model = Suco
    template_name = 'detalhe_suco.html'


class RefrigeranteListView(generic.ListView):
    model = Refrigerante
    queryset = Refrigerante.objects.all()
    template_name = 'lista_refrigerante.html'


class RefrigeranteDetailView(generic.DetailView):
    model = Refrigerante
    template_name = 'detalhe_refrigerante.html'


class FritasListView(generic.ListView):
    model = Fritas
    queryset = Fritas.objects.all()
    template_name = 'lista_fritas.html'


class FritasDetailView(generic.DetailView):
    model = Fritas
    template_name = 'detalhe_fritas.html'


class SaladasListView(generic.ListView):
    model = Saladas
    queryset = Saladas.objects.all()
    template_name = 'lista_saladas.html'


class SaladasDetailView(generic.DetailView):
    model = Saladas
    template_name = 'detalhe_saladas.html'

# Create your views here.
