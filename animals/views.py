from django.shortcuts import render
from .models import Category, Curator, Animal
from django.views.generic import ListView, DetailView


# Create your views here.
class PageView(ListView):
    model = Animal
    context_object_name = 'animal'
    template_name = 'animals/Base.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "All animals"
        return context


class CuratorsView(ListView):
    model = Curator
    context_object_name = 'curator'
    template_name = 'curators/all_curators.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "All curators"
        return context


class AnimalByCategory(ListView):
    model = Animal
    context_object_name = 'animalcat'
    template_name = 'animals/current_animal.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return Animal.objects.filter(category_id=self.kwargs['category_id'])


class CuratorDetails(DetailView):
    model = Curator
    pk_url_kwarg = "curator_id"
    context_object_name = "curator"

    template_name = 'curators/curator_details.html'




class AnimalsDetails(DetailView):
    model=Animal
    pk_url_kwarg = "animal_id"
    context_object_name = "anim"
    template_name = 'animals/current_animal.html'
