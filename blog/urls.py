from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="blog-home"),
    path('ourSponsors', views.home, name="blog-our-sponsors"),
    path('gallery', views.home, name="blog-gallery"),
    path('ourJourney', views.home, name="blog-our-journey"),
    path('aboutUs', views.home, name="blog-about-us"),
]
