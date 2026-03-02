from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("card/", views.view_card, name="view_card")
]