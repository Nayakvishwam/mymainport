from django.shortcuts import render, HttpResponse, redirect
from rest_framework.response import Response
from django.contrib import messages
from .models import *
from django.core.mail import send_mail
from rest_framework.decorators import api_view
import json
import random
from django.forms.models import model_to_dict
from django.db.models import Max
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from .forms import *
from django.conf import settings
# Create your views here.


def index(request):
    return render(request, 'index.html')


def logout(request):
    if request.session.has_key("is_user"):
        del request.session['is_user']
    return redirect('/')


def contact(request):
    if request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        data = ccontactme(name=name, email=email, message=message)
        data.save()
    return render(request, 'contact.html')


@api_view(['POST'])
def createapi(request):
    data = ccontactme.objects.all()
    maindict = {}
    ldata = []
    for i in data.iterator():
        maindict[f'name'] = i.name
        maindict[f'email'] = i.email
        maindict[f'message'] = i.message
        ldata.append(maindict)
        # maindict={f'name{i.id}':i.name,f'email{i.id}':i.email,f'message{i.id}':i.message}
    return JsonResponse(ldata)


def deletedata(request, myid):
    if request.session.has_key("is_user"):
        data = ccontactme.objects.get(id=myid)
        data.delete()
        return redirect('/admin/')
    else:
        return redirect('/')


def showallprojects(request):
    data = addprojects.objects.all()
    l = []
    l.append(data)
    return render(request, 'projectsshow.html', {'data': l})


def myinfo(request):
    data = mydata.objects.aggregate(Max('id'))
    o = []
    for i in data.values():
        maindata = mydata.objects.get(id=i)
        o = maindata
    return render(request, 'about.html', {'data': o})


def adddetails(request):
    if request.session.has_key("is_user"):
        form = adddeatislofuser()
        context = {'form': form}
        if request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            Address = request.POST.get('Address')
            age = request.POST.get('age')
            Phonenumber = request.POST.get('Phonenumber')
            Skills = request.POST.get('Skills')
            Collegename = request.POST.get('Collegename')
            email = request.POST.get('email')
            myfile = request.FILES.get('media')
            myfilesecond = request.FILES.get('image')
            fs = FileSystemStorage()
            filname = fs.save(myfile.name, myfile)
            url = fs.url(myfile)
            filnamesecond = fs.save(myfilesecond.name, myfilesecond)
            urlsecond = fs.url(myfilesecond)
            dta = mydata(name=name, image=urlsecond, Address=Address, age=age, email=email,
                         Phonenumber=Phonenumber, Skills=Skills, Collegename=Collegename, media=url)
            dta.save()
        else:
            form = adddeatislofuser()
        return render(request, 'adddeatils.html', context=context)
    else:
        return redirect('/')


def forgot(request):
    if request.POST:
        email = request.POST.get('email')
        data = resgister.objects.filter(email=email).count()
        datamain = resgister.objects.filter(email=email)
        forgot.dataall = datamain
        ot = random.randint(2000, 9999)
        forgot.email = email
        forgot.otp = ot
        if data > 0:
            return render(request, 'changepassword.html',{'data':ot,'email':email})
        else:
            messages.error(request, 'This email is not used for register')
            return redirect('forgot')
    return render(request, 'changepassword.html')


def addproject(request):
    if request.session.has_key("is_user"):
        if request.POST:
            techdata = request.POST.get('tech')
            heading = request.POST.get('title')
            link = request.POST.get('link')
            data = addprojects(techdata=techdata, head=heading, link=link)
            data.save()
        return render(request, 'addproject.html')
    else:
        return redirect('/')


def showallmydata(request):
    if request.session.has_key("is_user"):
        data = mydata.objects.all()
        l = []
        l.append(data)
        return render(request, 'showme.html', {'data': l})
    else:
        return redirect('/')


def addnew(request):
    if request.POST:
        email=request.POST.get('email')
        password=request.POST.get('pass')
        confirm=request.POST.get('cp')
        name=request.POST.get('name')
        if resgister.objects.filter(email=email).exists():
            messages.error(request, 'email alrady using for register')
            return redirect('addnew')
        else:
            data=resgister(name=name,email=email,passwords=password)
            data.save()
            messages.success(request, 'Register succesfully')
            return redirect('logindata')
    return render(request, 'addadmin.html')


def adminfirst(request):
    if request.session.has_key("is_user"):
        data = ccontactme.objects.all()
        alldata = []
        alldata.append(data)
        return render(request, "adminindex.html", {'data': alldata})
    else:
        return redirect('/')


def lgin(request):
    if request.session.has_key("is_user"):
        return redirect('/admin/')
    elif request.POST:
        email = request.POST.get('email')
        password = request.POST.get('password')
        data = resgister.objects.filter(
            email=email, passwords=password).count()
        if data > 0:
            request.session["is_user"] = True
            return redirect('/admin/')
        else:
            messages.error(request, 'Wrong password or email id')
            return redirect('logindata')
    return render(request, 'login.html')


def deleteone(request, myid):
    if request.session.has_key("is_user"):
        data = mydata.objects.get(id=myid)
        data.delete()
        return redirect('shwomydata')
    else:
        return redirect('/')


def checkotp(request):
    otp = forgot.otp
    if request.POST:
        ot = request.POST.get('otp')
        password = request.POST.get('password')
        againpassword = request.POST.get('confirmpassword')
        if int(ot) != otp:
            messages.error(request, 'Enter valid otp')
            return redirect('check')
        else:
            for i in forgot.dataall.iterator():
                data = resgister(id=i.id, email=forgot.email,
                                 passwords=password)
                data.save()
            messages.success(request, 'Chenge password succesfully')
            return redirect('logindata')
    return render(request, 'checkotp.html', {'data': otp})
