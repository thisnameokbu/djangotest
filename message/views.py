from django.shortcuts import render
from .models import UserMessage

def getform(request):
    return render(request, 'message_form.html')

def newmessage(request):
    if request.method == 'POST':
        user_message = UserMessage()
        user_message.name = request.POST.get('name')
        user_message.email = request.POST.get('email')
        user_message.address = request.POST.get('address')
        user_message.message = request.POST.get('message')
        user_message.save()
    return render(request, 'message_form.html')

