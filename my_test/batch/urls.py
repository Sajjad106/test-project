from . import views as v 
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', v.batch, name='batch'),

]
