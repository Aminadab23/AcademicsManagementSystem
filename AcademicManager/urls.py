from django.urls import path
from . import views
urlpatterns = [
    path('add_coordinator', views.addCoordinator, name= 'add-coordinator'),
    path('AcMhome', views.home, name='ahome'),
    path('add_academy', views.addAcademy, name= 'add-academy'),
    path('addcfinish', views.validate, name= 'addcfinish'),
    path('ictdesc', views.describe, name='description'),
    path('usermessages', views.mess, name='usermessage'),


]
