from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Card
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to My Greeting App 🎉</h1>")

def view_card(request):
    name = request.GET.get('name', 'Serena, My Love')
    message = request.GET.get('msg', 'Hey love, I just wanted to remind you how special you are to me. Your smile, your heart, and the way you care for others make my world brighter every single day. I’m really grateful to have you in my life. 💛')
    return render(request, 'cards/card.html', {'card': {'recipient_name': name, 'message': message}})