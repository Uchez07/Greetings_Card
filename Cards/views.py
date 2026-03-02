from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Card
from django.http import HttpResponse

def view_card(request):
    name = request.GET.get('name', 'Serena, My Love')
    message = request.GET.get('msg', 'Love')
    return render(request, 'Cards/card.html', {'card': {'recipient_name': name, 'message': message}})