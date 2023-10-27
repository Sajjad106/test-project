from . import views as v 
from django.urls import path

urlpatterns = [
    path('admin/', v.class_index, name='grades'),
    path('admin/grades_insert', v.class_insert, name='class_info_insert')
]
