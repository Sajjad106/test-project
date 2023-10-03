from . import views as v 
from django.contrib import admin
from django.urls import path,  include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentadmin/', v.student, name= 'studentadmin'),
    path('insert/', v.insert, name='student_info_insert'),
    path('edit/<int:id>', v.edit_index, name='edit_index'),
    path('delete/<int:id>', v.delete_index, name='delete_index'),
    path('update/', v.update, name='student_info_update'),
    path('studentadmin/', v.student, name= 'studentadmin'),
    path('batch/', include('batch.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
