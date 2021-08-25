from django.urls import path
from .views import *

urlpatterns=[

    path('',views.MainPage, name='main_animals'),
    path('mailing/',views.mess, name='mess'),
    path('registration/',views.registration, name='registration'),
    path('site_login/',views.site_login, name='site_login'),
    path('site_logout/', views.site_logout, name='site_logout'),
    path('animals/',PageView.as_view(), name='all_animals'),
    path('animals/curators/', CuratorsView.as_view(), name='all_curators'),
    path('animals/<int:category_id>',AnimalByCategory.as_view(),name='category'),
    path('animals/<int:animal_id>/', AnimalsDetails.as_view(),name='details'),
    path('animals/curators/<int:curator_id>',CuratorDetails.as_view(),name='curator_details'),
    path('animals/add_animal/',CreateAnimal.as_view(),name='add_animal'),
    path('animals/add_curator/',CreateCurator.as_view(),name='add_curator'),

    path('animals/news/',NewsView.as_view(),name='news'),

]