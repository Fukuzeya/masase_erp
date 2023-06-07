from django.db import models
from django.conf import settings
import json
from django.db.models.signals import post_save,pre_delete
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

from twilio.rest import Client

# Create your models here.


class Transaction(models.Model):
    title = models.CharField(max_length=100)
    forename = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    bank = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    
    


@receiver(post_save, sender=Transaction)
def send_welcome_message(sender, instance, created, **kwargs):
    if created:
        # Get the Twilio account SID and auth token from your environment variables
        account_sid = 'ACd526e2f40c37ae32b76babae29fa4a32'
        auth_token = 'f564a96189879158d6ee6cf94ab59d87'

        # Create a Twilio client
        client = Client(account_sid, auth_token)
        text = f"Hi {instance.title} {instance.forename} {instance.surname}, your loan has been approved by POSB"
        # Get the user's phone number
        phone_number = instance.phone_number
        phone_number = "+263"+str(phone_number)

        # Send a text message
        client.messages.create(
            to=phone_number,
            from_='+12545564762',
            body=text
        )
        
        
class Loan(models.Model):
    branch_code = models.CharField(max_length=100,null=True,blank=True)
    branch_name = models.CharField(max_length=100,null=True,blank=True)
    title = models.CharField(max_length=100,null=True,blank=True)
    gender = models.CharField(max_length=100,null=True,blank=True)
    forenames = models.CharField(max_length=100,null=True,blank=True)
    surname = models.CharField(max_length=100,null=True,blank=True)
    idno = models.CharField(max_length=100,null=True,blank=True)
    dob = models.CharField(max_length=100,null=True,blank=True)
    nationality =models.CharField(max_length=100,null=True,blank=True)
    citizenship = models.CharField(max_length=100,null=True,blank=True)
    defaulthistory = models.CharField(max_length=100,null=True,blank=True)
    mainincomesource = models.CharField(max_length=100,null=True,blank=True)
    empolymenttype = models.CharField(max_length=100,null=True,blank=True)
    netincome = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    bank= models.CharField(max_length=100,null=True,blank=True)
    branch = models.CharField(max_length=100,null=True,blank=True)
    bankaccountno = models.CharField(max_length=100,null=True,blank=True)
    accountsotherbanks = models.BooleanField(default=False)
    otherpropertyowenership = models.CharField(max_length=100,null=True,blank=True)
    nextofkinrelatioship = models.CharField(max_length=100,null=True,blank=True)
    periodinmonths = models.IntegerField(null=True, blank=True)
    usacitizenship = models.CharField(max_length=100,null=True,blank=True)
    usaresidentcard = models.CharField(max_length=100,null=True,blank=True)
    no_dependants = models.IntegerField(null=True,blank=True)
    street_number = models.IntegerField(null=True,blank=True)
    town= models.CharField(max_length=100,null=True,blank=True)
    postaladdress = models.CharField(max_length=100,null=True,blank=True)
    home_type = models.CharField(max_length=100,null=True,blank=True)
    home_length = models.IntegerField(null=True,blank=True)
    phone_no = models.CharField(max_length=100,null=True,blank=True)
    email= models.CharField(max_length=100,null=True,blank=True)
    initials = models.CharField(max_length=100,null=True,blank=True)
    insolvent = models.CharField(max_length=100,null=True,blank=True)
    marital_status = models.CharField(max_length=100,null=True,blank=True)
    insolventdetail = models.CharField(max_length=100,null=True,blank=True)
    microfinancerelated = models.CharField(max_length=100,null=True,blank=True)
    microfinancerelatedname = models.CharField(max_length=100,null=True,blank=True)
    curr_employer = models.CharField(max_length=100,null=True,blank=True)
    current_empl_adress = models.CharField(max_length=100,null=True,blank=True)
    curr_emp_length_year = models.IntegerField(null= True,blank=True)
    employer_contact_person= models.CharField(max_length=100,null=True,blank=True)
    curr_emp_phone = models.CharField(max_length=100,null=True,blank=True)
    curr_emp_email = models.CharField(max_length=100,null=True,blank=True)
    curr_emp_position = models.CharField(max_length=100,null=True,blank=True)
    nextofkin_rel_name = models.CharField(max_length=100,null=True,blank=True)
    nextofkin_rel_add = models.CharField(max_length=100,null=True,blank=True)
    next_of_kin_employer_name = models.CharField(max_length=100,null=True,blank=True)
    nextofkin_rel_phone = models.CharField(max_length=100,null=True,blank=True)
    nextofkin_rel_reltnshp = models.CharField(max_length=100,null=True,blank=True)
    ecno = models.CharField(max_length=100,null=True,blank=True)
    civiljudgements = models.CharField(max_length=100,null=True,blank=True)
    sectioncode = models.CharField(max_length=100,null=True,blank=True)
    currency = models.CharField(max_length=100,null=True,blank=True)
    fin_amt = models.DecimalField(decimal_places=2, max_digits=10,null=True,blank=True)
    fin_tenor = models.IntegerField(null=True,blank=True)
    fin_int_rate = models.IntegerField(null=True,blank=True)
    fin_purpose = models.CharField(max_length=100,null=True,blank=True)
    fin_repay_date = models.DateField(null=True,blank=True)
    applied_date = models.DateField(null=True,blank=True)
    recommended_amt = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    created_by = models.CharField(max_length=100,null=True,blank=True)
    finproducttype = models.CharField(max_length=100,null=True,blank=True)
    sector= models.CharField(max_length=100,null=True,blank=True)
    currborrowings = models.CharField(max_length=100,null=True,blank=True)
    prevborrowings = models.CharField(max_length=100,null=True,blank=True)
    repaymentintervalnum = models.IntegerField(null=True,blank=True)
    repaymentunitinterval = models.CharField(max_length=100,null=True,blank=True)
    adminrate = models.IntegerField(null=True,blank=True)
    monthly_payment = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    agent_reference = models.CharField(max_length=100,null=True,blank=True)
    ssb_reference = models.CharField(max_length=100,null=True,blank=True)
    refund_bank_name = models.CharField(max_length=100,null=True,blank=True)
    refund_branch_name = models.CharField(max_length=100,null=True,blank=True)
    refund_account_number  = models.CharField(max_length=100,null=True,blank=True)
    sales_rep = models.CharField(max_length=100,null=True,blank=True)
    delivery_status = models.CharField(max_length=100,default="Not Delivered",null=True,blank=True)
    loan_reference = models.CharField(max_length=100,null=True, blank=True)
    loan_status = models.BooleanField(default=False)
    date_created= models.DateField(auto_now_add=True,null=True,blank=True)
    
    #functions
    
    @property
    def is_black_listed(self):
        pass
    
    @property
    def get_net_disbasement(self):
        pass
    
    @property
    def get_agent_commission(self):
        pass
    
    @property
    def get_days_before_delivery(self):
        pass
        
    
    
    class Meta:
        verbose_name = "Loan"
        verbose_name_plural = "Loans"

@receiver(post_save, sender=Loan)
def generate_loan_reference(sender, instance, created, **kwargs):
    if created:
        #check if there is already existing reference
        if Loan.objects.all().exists():
            loan_count = Loan.objects.all().count()
            today = datetime.datetime.today().date()
            date_str = str(today)
            ref = date_str.replace("-","") + str(loan_count + 1)
            instance.loan_reference = ref
            instance.save()
        else:
            # no existing reference found
            today = datetime.datetime.today().date()
            count = 1
            date_str = str(today)
            ref = date_str.replace("-","") + str(count)
            instance.loan_reference = ref
            instance.save()
            

class Response(models.Model):
    recid = models.CharField(max_length=100,null=True, blank=True)
    deductioncode = models.CharField(max_length=100,null=True, blank=True)	
    reference = models.CharField(max_length=100,null=True, blank=True)
    idnumber = models.CharField(max_length=100,null=True, blank=True)
    ecnumber= models.CharField(max_length=100,null=True, blank=True)
    type = models.CharField(max_length=100,null=True, blank=True)
    status = models.CharField(max_length=100,null=True, blank=True)
    startdate = models.DateField(null=True, blank=True)
    enddate = models.DateField(null=True, blank=True)
    amount = models.DecimalField(decimal_places=2,max_digits=10,null=True,blank=True)
    name = models.CharField(max_length=100,null=True, blank=True)
    bankaccount = models.CharField(max_length=100,null=True, blank=True)
    message = models.CharField(max_length=100,null=True, blank=True)
    date_received = models.DateField(auto_now_add=True)    
    


account_sid = 'ACd526e2f40c37ae32b76babae29fa4a32'
auth_token = 'f564a96189879158d6ee6cf94ab59d87'

        # Create a Twilio client
client = Client(account_sid, auth_token)



@receiver(post_save, sender=Response)
def udate_loan_status(sender, instance, created, **kwargs):
    if created:
        loans = Loan.objects.filter(loan_status = False)
        for loan in loans:
            if str(loan.loan_reference) == str(instance.reference):
                if str(instance.status).lower() == "success":
                    loan.loan_status= True
                    loan.save()
                    text = f"Hi {loan.title} {loan.forenames} {loan.surname}, your loan for {loan.fin_purpose} has been approved."
                    # Get the user's phone number
                    phone_number = loan.phone_no
                    phone_number = "+263"+str(phone_number)
                    print(text)
                    # Send a text message
                    client.messages.create(
                        to=phone_number,
                        from_='+12545564762',
                        body=text
                    )
                else:
                    text = f"Hi {loan.title} {loan.forenames} {loan.surname}, your loan for {loan.fin_purpose} has been rejected because of {instance.message}."
                    # Get the user's phone number
                    phone_number = loan.phone_no
                    phone_number = "+263"+str(phone_number)
                    print(text)
                    #Send a text message
                    client.messages.create(
                        to=phone_number,
                        from_='+12545564762',
                        body=text
                    )
                    
                    
                    
                
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    