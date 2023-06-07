from django.shortcuts import render
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# from .forms import *
from .models import *
from Accounts.views import is_agent
from .forms import *
# Create your views here.


@login_required
def agent_profile(request):
    if not is_agent(request.user):return redirect("accounts:login")
    national_id = request.user.first_name
    agent = Agent.objects.get(national_id = national_id)
    return render(request,'agent/profile.html')

def application_process_one(request):
    if request.method =='POST':
        form = ApplicationForm1(request.POST,request.FILES)
        if form.is_valid():
            application_id = form.save()
            request.session['application_id'] = application_id.id
            return redirect("agent:stage_two")
    else:
        form = ApplicationForm1()
    return render(request,'agent/application1.html',{'form':form})

def application_process_two(request):
    app_id = request.session.get('application_id')
    if not app_id:
        return redirect("agent:stage_1")
    if request.method =='POST':
        form = ApplicationForm2(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            applicant = Applicant.objects.get(id=app_id)
            application.applicant = applicant
            application.save()
            return redirect("agent:stage_three")
    else:
        form = ApplicationForm2()
    return render(request,'agent/application2.html',{'form':form})

def application_process_three(request):
    app_id = request.session.get('application_id')
    if not app_id:
        return redirect("agent:stage_1")
    if request.method =='POST':
        form = ApplicationForm3(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            applicant = Applicant.objects.get(id=app_id)
            application.applicant = applicant
            application.save()
            return redirect("agent:stage_four")
    else:
        form = ApplicationForm3()
    return render(request,'agent/application3.html',{'form':form})

def application_process_four(request):
    app_id = request.session.get('application_id')
    if not app_id:
        return redirect("agent:stage_1")
    if request.method =='POST':
        form = ApplicationForm4(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            applicant = Applicant.objects.get(id=app_id)
            application.applicant = applicant
            application.save()
            return redirect("agent:stage_five")
    else:
        form = ApplicationForm4()
    return render(request,'agent/application4.html',{'form':form})

def application_process_five(request):
    national_id = request.user.first_name
    agent = Agent.objects.get(national_id = national_id)
    app_id = request.session.get('application_id')
    if not app_id:
        return redirect("agent:stage_1")
    if request.method =='POST':
        form = ApplicationForm5(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            applicant = Applicant.objects.get(id=app_id)
            application.applicant = applicant
            application.save()
            #Assign agent to applicant
            applicant.agent = agent
            return redirect("agent:agent_profile")
    else:
        form = ApplicationForm5()
    return render(request,'agent/application5.html',{'form':form})


