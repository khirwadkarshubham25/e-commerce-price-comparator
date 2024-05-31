from django.urls import path

from ecommerce_scraper import views

urlpatterns = [
    path("home", views.Home.as_view(), name='home')
]
