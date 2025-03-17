from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
import os
from django.conf import settings
from .models import AboutMe, Project, Certificate
from dotenv import load_dotenv
load_dotenv()

def home(request):
    about_me = AboutMe.objects.first()
    about_text = about_me.text if about_me else "Text not available."
    projects = Project.objects.all()
    certificates = Certificate.objects.all()
    
    return render(request, 'index.html', {
        'about_me': about_text,
        'projects': projects,
        'certificates': certificates,
        })

def send_email(request):
    if request.method == "POST":
        message = request.POST.get('message')
        if message:
            
            send_mail(
                'New message from portfolio',
                message,
                os.getenv('GMAIL_NAME'),
                [os.getenv('GMAIL_NAME')],
            )
            
            messages.success(request, 'Message sent successfully!')
            return redirect('home')
        else:
            messages.error(request, 'No message provided!')
            return redirect('home')
    else:
        return redirect('home')
    
