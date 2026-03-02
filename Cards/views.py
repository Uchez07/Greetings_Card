from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Card
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to My Greeting App 🎉</h1>")

def view_card(request):
    name = request.GET.get('name', 'Serena, My Love')
    message = request.GET.get('msg', 'Love')
    return render(request, 'cards/card.html', {'card': {'recipient_name': name, 'message': message}})