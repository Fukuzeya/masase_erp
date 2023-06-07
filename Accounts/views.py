from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .forms import *


def is_client(user):
    return user.groups.filter(name='clients').exists()
def is_agent(user):
    return user.groups.filter(name='agents').exists()
def is_admin(user):
    return user.groups.filter(name='admins').exists()

def home_page(request):
    return render(request,"index.html")
#student account
def client_account_creation(request):
    if request.method =='POST':
        form = ClientSignUp(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            group  = Group.objects.get(name="agents")
            user.save()
            group.user_set.add(user)
            return redirect('accounts:login')
    else:
        form = ClientSignUp()
    return render(request,'auth/client/auth-sign-up.html',{'form':form})

def agent_account_creation(request):
    if request.method =='POST':
        form = AgentSignUp(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            group  = Group.objects.get(name="clients")
            user.save()
            group.user_set.add(user)
            return redirect('accounts:login')
    else:
        form = AgentSignUp()
    return render(request,'auth/agent/auth-sign-up.html',{'form':form})


@login_required
def profile_check(request):
    if is_client(request.user):
        return redirect("applicant:client_profile")
    elif is_agent(request.user):
        return redirect("agent:agent_profile")
    # elif is_admin(request.user):
    #     return redirect("accounts:admin_profile")
    # else:
    #     return redirect("accounts:login")
    
# @login_required
# def student_dashboard(request):
#     if is_student(request.user):
#         student_id = request.user.first_name
#         student = Student.objects.get(student_id = student_id)
#         if not student.student_contact:
#             return redirect("accounts:student")
#         return render(request,'student/dashboard.html',{'student':student})
#     else:
#         return redirect('accounts:profile')
# @login_required
# def teacher_dashboard(request):
#     if is_teacher(request.user):
#         ec_number = request.user.first_name
#         teacher = Teacher.objects.get(ec_number = ec_number)
#         return render(request,'teacher/dashboard.html',{'teacher':teacher})
#     else:
#         return redirect('accounts:profile')
# @login_required
# def admin_dashboard(request):
#     if is_admin(request.user):
#         return render(request,'admins/dashboard.html')
#     else:
#         return redirect('accounts:profile')

