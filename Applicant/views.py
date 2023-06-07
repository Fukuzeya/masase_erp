from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def client_profile(request):
    ec_number = request.user.first_name
    emp = EmploymentDetails.objects.get(employee_number = ec_number)
    client = Applicant.objects.get(id = emp.applicant.id)
    return render(request,'client/profile.html',{'client':client})

def get_available_products(request):
    products =Product.objects.all()
    return render(request,'client/products.html',{'products':products})

def loan_application(request,id):
    product = Product.objects.get(id=id)
    if request.method =='POST':
        form = LoanForm(request.POST,request.FILES)
        loan_tenure = request.POST.get('loan_tenure')
        loan_amount = 0.0
        monthly_amount = 0.0
        if loan_tenure == '3 months':
            amount = (product.price /3)
            monthly_amount = (float(amount) * 0.03) + float(amount)
            loan_amount = monthly_amount * 3
        elif loan_tenure == '6 months':
            amount = (product.price /6)
            monthly_amount = (float(amount) * 0.03) + float(amount)
            loan_amount = monthly_amount * 6
        elif loan_tenure == '12 months':
            amount = (product.price /12)
            monthly_amount = (float(amount) * 0.03) + float(amount)
            loan_amount = monthly_amount * 12
        elif loan_tenure == '24 months':
            amount = (product.price /24)
            monthly_amount = (float(amount )* 0.03) + float(amount)
            loan_amount = monthly_amount * 24
        
        if form.is_valid():
            loan = form.save(commit=False)
            applicant = Applicant.objects.all().last()
            loan.applicant = applicant
            loan.loan_purpose  = product.name
            loan.product = product
            loan.loan_amount = loan_amount
            loan.monthly_installment = monthly_amount
            loan.save()
            request.session['loan_id'] = loan.id
            return render(request,'client/loan-confirmation.html',{'loan':loan,'montly_amount':monthly_amount})
    else:
        form = LoanForm()
    return render(request,'client/loan-application.html',{'form':form,'product':product})

def confirm_loan(request):
    if request.method == "POST":
        payslip = request.FILES.get('payslip')
        national_id = request.FILES.get('national_id')
        loan_id = request.session.get('loan_id')
        loan = LoanDetails.objects.get(id=loan_id)
        loan.payslip = payslip
        loan.national_id = national_id
        loan.has_confirmed =True
        loan.save()
        return redirect('applicant:applied_loans')

def get_my_loans(request):
    ec_number = request.user.first_name
    emp = EmploymentDetails.objects.get(employee_number = ec_number)
    applicant = Applicant.objects.get(id = emp.applicant.id)
    loans = applicant.loan_details.all()
    return render(request,'client/loans.html',{'loans':loans})

def application_process_one(request):
    if request.method =='POST':
        form = ApplicationForm1(request.POST,request.FILES)
        if form.is_valid():
            application_id = form.save()
            request.session['application_id'] = application_id.id
            return redirect("applicant:app_process_two")
    else:
        form = ApplicationForm1()
    return render(request,'application1.html',{'form':form})

def application_process_two(request):
    app_id = request.session.get('application_id')
    # if not app_id:
    #     return redirect("applicant:app_process_one")
    if request.method =='POST':
        form = ApplicationForm2(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            applicant = Applicant.objects.get(id=app_id)
            application.applicant = applicant
            application.save()
            return redirect("applicant:app_process_three")
    else:
        form = ApplicationForm2()
    return render(request,'application2.html',{'form':form})

def application_process_three(request):
    app_id = request.session.get('application_id')
    # if not app_id:
    #     return redirect("applicant:app_process_one")
    if request.method =='POST':
        form = ApplicationForm3(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            applicant = Applicant.objects.get(id=app_id)
            application.applicant = applicant
            application.save()
            return redirect("applicant:app_process_four")
    else:
        form = ApplicationForm3()
    return render(request,'application3.html',{'form':form})

def application_process_four(request):
    app_id = request.session.get('application_id')
    # if not app_id:
    #     return redirect("applicant:app_process_one")
    if request.method =='POST':
        form = ApplicationForm4(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            applicant = Applicant.objects.get(id=app_id)
            application.applicant = applicant
            application.save()
            return redirect("applicant:app_process_five")
    else:
        form = ApplicationForm4()
    return render(request,'application4.html',{'form':form})

def application_process_five(request):
    app_id = request.session.get('application_id')
    # if not app_id:
    #     return redirect("applicant:app_process_one")
    if request.method =='POST':
        form = ApplicationForm5(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            applicant = Applicant.objects.get(id=app_id)
            application.applicant = applicant
            application.save()
            return redirect("applicant:client_profile")
    else:
        form = ApplicationForm5()
    return render(request,'application5.html',{'form':form})