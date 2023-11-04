from django.urls import path
from . import views # From current folder, import views module

# URL Configuration
# URLconf
urlpatterns = [
    #path('hello/', views.say_hello)
    path('', views.home, name='home'),
]