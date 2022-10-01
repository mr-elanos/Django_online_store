from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import *
from .forms import ContactForm

menu = [{'title': 'ГОЛОВНА', 'url_name': 'home'},
        {'title': 'НАШІ ПРИЧЕПИ', 'url_name': 'all_categories'},
        {'title': 'ДОСТАВКА І ОПЛАТА', 'url_name': 'buy_and_delivery'},
        {'title': 'КОНТАКТИ', 'url_name': 'contacts'},
        {'title': 'ПРО НАС', 'url_name': 'about'}
        ]


def index(request):
    return render(request, 'pages/index.html', {'menu': menu, 'title': 'Завод автомобільних причепів MAG Trailer'})


class AllCategories(ListView):
    model = Product
    template_name = 'pages/categories.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Наші причепи'
        context['cat_selected'] = None
        return context

    def get_queryset(self):
        return Product.objects.filter(available=True)


class ShowCategories(ListView):
    model = Product
    template_name = 'pages/categories.html'
    context_object_name = 'products'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Категорія: ' + str(context['products'][0].category)
        context['cat_selected'] = context['products'][0].category_id
        return context

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['cat_slug'], available=True)


class ShowProduct(DetailView):
    model = Product
    template_name = 'pages/product.html'
    slug_url_kwarg = 'product_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['product'].name
        context['photos'] = ProductImages.objects.filter(product_id=context['product'].id)
        return context


def buy_and_delivery(request):
    return render(request, 'pages/buy_and_delivery.html', {'menu': menu, 'title': 'Доставка і оплата'})


class Contacts(CreateView):
    form_class = ContactForm
    template_name = 'pages/contacts.html'
    success_url = reverse_lazy('ok_form')

    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Контакти'
        context['menu'] = menu
        return context


def ok_form(request):
    return render(request, 'pages/ok_form.html', {'menu': menu, 'title': 'Звернення прийнято', })


def about(request):
    return render(request, 'pages/about.html', {'menu': menu, 'title': 'Про підприємство'})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Сторінка не знайдена :(</h1>')
