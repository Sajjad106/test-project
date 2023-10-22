from . import views as v 
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', v.batch, name='batch'),
    path('admin/batch_insert', v.batch_insert ,name='batch_info_insert'),

]
