from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('home', views.home, name= 'chome'),
    path('addCourse', views.addcourse, name= 'add-course'),
    path('addStudent', views.addStudent, name= 'addStudent'),
    path('validate', views.validate, name= 'validate'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)