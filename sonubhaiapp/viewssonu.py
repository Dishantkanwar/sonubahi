import email
from django.http import HttpResponse
from django.shortcuts import render
from pendulum import today
from.models import *

def home(request):
    return render(request,'homepagesonu.html')
def about(request):
    return render(request,'aboutuspagesonu.html')
def tracking(request):
    return render(request,'trackcamppage.html') 
    
def hp(request):
    return render(request,'hp.html') 
def jk(request):
    return render(request,'jk.html') 
def uk(request):
    return render(request,'uk.html') 
def bookingg(request):
     if request.method=='POST':
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        today=request.POST['today']
        state=request.POST['state']
        places=request.POST['places']
        date=request.POST['date']
        enddate=request.POST['enddate']
        obj=booket()
        obj.Name=name
        obj.Phone=phone
        obj.Email=email
        obj.Today=today
        obj.State=state
        obj.Places=places
        obj.Date=date
        obj.Enddate=enddate
        obj.save()
        return render(request,'payment.html')
     return render (request,'booking.html')

def contact(request):
    if request.method=='POST':
        name=request.POST['your_name']
        email=request.POST['your_email']
        phone=request.POST['your_phone']
        problem=request.POST['your_problem']
        obj= contact_us()
        obj.yourname=name
        obj.youremail=email
        obj.yourphone=phone
        obj.yourproblem=problem
        obj.save()
        return HttpResponse('YOUR PROBLEM IS SENDED SUCCESSFULLY AND OUR  TECHICAL TEAM WILL  CALL YOU !!!')
    return render(request,'contactuspage.html')

def test1(request):
    return render(request,'test.html')
def payment(request):
    return render(request,'payment.html')

