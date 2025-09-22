from django.urls import path

from . import views
app_name='job'

urlpatterns = [
    path('singup',views.signup,name='singup'),
    path('profile',views.profile,name='profile'),
    path('profile_edit',views.profile_edit,name='profile_edit'),


]
