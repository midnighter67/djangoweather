from django.urls import path
from . import views # '.' is current directory

urlpatterns = [
    # add urls for each webpage here
    path('', views.home, name="home"),
    path('about.html', views.about, name="about"),
]
