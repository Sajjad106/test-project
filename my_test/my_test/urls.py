from . import views as v 
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentadmin/', v.student, name= 'studentadmin'),
    path('insert/', v.insert, name='student_info_insert'),
    path('edit/<int:id>', v.edit_index, name='edit_index'),
    path('delete/<int:id>', v.delete_index, name='delete_index'),
    path('update/', v.update, name='student_info_update'),
]
