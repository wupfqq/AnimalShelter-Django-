from django.urls import path
from .views import *

urlpatterns=[
    path('', PageView.as_view(), name='all_animals'),
    path('curators/', CuratorsView.as_view(), name='all_curators'),
    path('<int:category_id>',AnimalByCategory.as_view(),name='category'),
    path('<int:animal_id>/', AnimalsDetails.as_view(),name='details'),
    path('curators/<int:curator_id>',CuratorDetails.as_view(),name='curator_details')
]