from django.urls import path
from .views import insert_form_data, home

urlpatterns = [

    path('insert-form-data/', insert_form_data, name='insert_form_data'),
    path('', home, name='home')
]
