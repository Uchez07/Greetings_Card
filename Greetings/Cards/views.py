from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Card

def view_card(request, card_id):
    card = get_object_or_404(Card, id=card_id)
    return render(request, "cards/card.html", {"card": card})