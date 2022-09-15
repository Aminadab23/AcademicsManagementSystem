from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('message', views.UserMess, name='message'),
    path('reciteUpload', views.reciteUpload, name= 'reciteUpload'),
    path('updateProfile', views.profile_update, name= 'updateProfile'),
    path('academic-detail', views.acdetail, name='academic-detail'),
    

]
