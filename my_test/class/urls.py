from . import views as v 
from django.urls import path

urlpatterns = [
    path('admin/', v.class_index, name='class'),
    path('admin/class_insert', v.class_insert, name='class_info_insert')
]
