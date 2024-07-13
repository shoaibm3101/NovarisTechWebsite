from django.shortcuts import render
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from .models import Applicant
import threading


class EmailThread(threading.Thread):
    def __init__(self, email_message):
        self.email_message = email_message
        threading.Thread.__init__(self)
    
    def run(self):
        self.email_message.send(fail_silently=False)

# Create your views here.
def home(request):
    return render(request, "homepage.html")

def service(request):
    return render(request, "servicepage.html")

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        position = request.POST['position']
        message = request.POST['message']
        resume = request.FILES['file']

        new_applicant = Applicant(name=name, email=email, position=position, message=message)
        new_applicant.save()


        email_message = EmailMessage("New Applicant", f"Name: {name}\nEmail: {email}\nPosition: {position}\nMessage: {message}", 'settings.EMAIL_HOST_USER', ['theonesm911@gmail.com'])
        email_message.attach(resume.name, resume.read(), resume.content_type)
        
        EmailThread(email_message).start()

    return render(request, "contactpage.html")

def about(request):
    return render(request, "aboutpage.html")