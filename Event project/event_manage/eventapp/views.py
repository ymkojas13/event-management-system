from django.shortcuts import render
from .models import mode
# Create your views here.
def home(request):
    return render(request,'home.html')

def aboutme(request):
    return render(request,'aboutme.html')

def resumeport(request):
    return render(request,'resumeport.html')

def contact(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(name)
        data = mode(name=name,subject=subject,email=email,message=message)
        data.save()
    return render(request,'contact.html')