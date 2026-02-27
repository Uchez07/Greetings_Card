from django.urls import path
from . import views

urlpatterns = [
    path("card/<uuid:card_id>/", views.view_card, name="view_card"),
]