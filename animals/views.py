from django.shortcuts import render, redirect
from .models import Category, Curator, Animal, News
from django.views.generic import ListView, DetailView, CreateView
from .forms import AnimalForm, CuratorForm, RegisterForm, SiteLogForm, MessForm
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . import views
from django.contrib.auth import login, logout
from django.core.mail import send_mail


# Create your views here.
def mess(request):
    if request.method == "POST":
        form = MessForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['state'], form.cleaned_data['body'],
                             'testdjango666@mail.ru', ['newtestdjango@mail.ru'],fail_silently=False)
            if mail:
                messages.success(request, "Mail is send to you!")
                return redirect('main_animals')
            else:

                messages.error(request, "Ooops, something goes wrong:(")
    else:
        form = MessForm()
    return render(request, "animals/mail.html", {"form": form})


def registration(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            us1 = form.save()
            login(request, us1)
            messages.success(request, "Now you're a part of out community!")
            return redirect('main_animals')
        else:

            messages.error(request, "Ooops, something goes wrong:(")
    else:
        form = RegisterForm()
    return render(request, "animals/registration.html", {"form": form})


def site_login(request):
    if request.method == "POST":
        form = SiteLogForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main_animals')
    else:
        form = SiteLogForm()

    return render(request, "animals/site_login.html", {"form": form})


def site_logout(request):
    logout(request)
    return redirect('main_animals')


def MainPage(request):
    return render(request, "animals/main_animal.html")


class PageView(ListView):
    model = Animal
    context_object_name = 'animal'
    template_name = 'animals/Base.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "All animals"
        return context


class NewsView(ListView):
    model = News
    context_object_name = 'news'
    template_name = 'animals/news.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "news"
        return context


class CuratorsView(ListView):
    model = Curator
    context_object_name = 'curator'
    template_name = 'curators/all_curators.html'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "curators"
        return context


class AnimalByCategory(ListView):
    model = Animal
    context_object_name = 'animalcat'
    template_name = 'animals/current_animal.html'
    paginate_by = 3

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
    model = Animal
    pk_url_kwarg = "animal_id"
    context_object_name = "anim"
    template_name = 'animals/current_animal.html'


class CreateAnimal(CreateView):
    form_class = AnimalForm
    template_name = "animals/add_animal.html"
    success_url = reverse_lazy('all_animals')


class CreateCurator(CreateView):
    form_class = CuratorForm
    template_name = "curators/add_curator.html"
    success_url = reverse_lazy('all_animals')

# def add_animal(request):
#   if request.method=='POST':
#      aform=AnimalForm(request.POST)
#     if aform.is_valid():
#        formy=aform.save()
#       return redirect(formy)
# else:
#   form=AnimalForm()
#  return render(request,"add_animal.html",{'form':form})
