from django.shortcuts import render,HttpResponseRedirect
from .models import registermodel
from .forms import registerform
from django.contrib import messages
from django.contrib.auth import login
# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    if request.method == 'POST':
        fm = registerform(request.POST)
        if fm.is_valid():
            firstnm = fm.cleaned_data['Firstname']
            lastnm = fm.cleaned_data['Lastname']
            ema = fm.cleaned_data['Email']
            con = fm.cleaned_data['Contact']
            addr = fm.cleaned_data['Address']
            gen = fm.cleaned_data['Gender']
            pa = fm.cleaned_data['Password']
            conp = fm.cleaned_data['Confirm_password']
            soco = fm.cleaned_data['Software_courses']
            registerstore = registermodel(Firstname=firstnm,Lastname=lastnm, Email=ema, Contact=con,Address=addr,Gender=gen,Password=pa,Confirm_password=conp,Software_courses=soco)
            registerstore.save()
            messages.success(request, 'You have register successfully')
            return HttpResponseRedirect('/register/')
    else:
        fm = registerform()
    data = registermodel.objects.all()
    return render(request, 'register.html', {'form': fm,'dataa': data})
def ulogin(request,id):
    if request.method == "POST":
        ui = registermodel.objects.get(pk=id)
        um = registerform(request.POST, instance=ui)
        if um.is_valid():
            uname = um.cleaned_data['Firstname']
            upass = um.cleaned_data['Password ']
            user = registermodel(Firstname=uname, Password=upass)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return HttpResponseRedirect('/ulogin')


def update_data(request,id):
    if request.method == "POST":
        pi=registermodel.objects.get(pk=id)
        fm=registerform(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'You have update successfully')
    else:
        pi=registermodel.objects.get(pk=id)
        fm=registerform(instance=pi)

    return render(request,'updateonline.html', {'form': fm})


def delete_data(request,id):
    if request.method == "POST":
        row = registermodel.objects.get(pk=id)
        row.delete()
        return HttpResponseRedirect('/register')

def contact(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(name)
        data = registermodel(name=name,subject=subject,email=email,message=message)
        data.save()
    return render(request,'contact.html')
def registershow(request):
    data = registermodel.objects.all()
    return render(request, 'registershow.html', {'dataa': data})


'''def aboutme(request):
    return render(request,'aboutme.html')

def resumeport(request):
    return render(request,'resumeport.html')

'''