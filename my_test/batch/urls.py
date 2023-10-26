from . import views as v 
from django.urls import path



urlpatterns = [
    path('admin/', v.batch, name='batch'),
    path('admin/batch_insert', v.batch_insert ,name='batch_info_insert'),
]
