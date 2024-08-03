from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    
    path('', views.home , name="home" ),
    path('home/', views.home , name="home" ),
    path('login/', views.login_view , name="login" ),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

]