from django.db import models

# Create your models here.
from Agent.models import Agent


titles =(
    ('Mr','Mr'),('Mrs','Mrs'),('Miss','Miss'),('Ms','Ms'),('Dr','Dr'),('Other','Other')
)
sex = (
    ('Male','Male'),('Female','Female'),('Others','Others')
)
marital_stats =(
    ('Married','Married'),('Single Never Married','Single Never Married'),('Divorced','Divorced'),('Widowed','Widowed'),('Engaged','Engaged')
)
rez =(
    ('Yes residing in Zimbabwe','Yes residing in Zimbabwe'),('No residing in another country','No residing in another country')
)

# New Application Table
class Applicant(models.Model):
    national_id = models.FileField(upload_to="files/",blank=True,null=True)
    title = models.CharField(max_length=100,choices=titles)
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    #maiden_name = models.CharField(max_length=100,null=True,blank=True,default="N/A")
    #number_of_dependants= models.CharField(max_length=100,null=True,blank=True,default="N/A")
    gender = models.CharField(max_length=100,choices=sex)
    marital_status = models.CharField(max_length=100,choices=marital_stats)
    dob = models.DateField()
    #country_of_birth = models.CharField(max_length=100)
    national_id_no = models.CharField(max_length=12)
    #residence_status = models.CharField(max_length=100,choices = rez)
    #current_citizenship = models.CharField(max_length=100)
    email = models.EmailField(null=True,blank=True)
    mobile_number = models.IntegerField()
    #home_telephone = models.IntegerField(null=True,blank=True)
    has_confirmed = models.BooleanField(default=False)
    agent = models.ForeignKey(Agent, null=True, blank=True, related_name='agent_clients',on_delete=models.DO_NOTHING)
    
#Applicant banking details
class BankDetails(models.Model):
    applicant = models.OneToOneField(Applicant,on_delete=models.CASCADE,related_name='bank_details')
    bank_name = models.CharField(max_length=100)
    branch_name = models.CharField(max_length=100)
    #bank_branch_code = models.CharField(max_length=100)
    #account_name = models.CharField(max_length=100)
    account_no = models.IntegerField()
    #account_type= models.CharField(max_length=100,null=True,blank=True,default='N/A')
    
rez_choice = (
    ('Owned','Owned'),('Rented','Rented'),('Stay with Parents','Stay with Parents')
)
#Applicant Address Details
class AddressDetails(models.Model):
    applicant = models.OneToOneField(Applicant,on_delete=models.CASCADE,related_name='address_details')
    resident = models.CharField(max_length=100,choices=rez_choice)
    address = models.TextField()
    street_name= models.CharField(max_length=100,null=True,blank=True)
    town = models.CharField(max_length=100,null=True,blank=True)
    #country = models.CharField(max_length=100,null=True,blank=True)
    #years_at_curent_res= models.IntegerField()
    
#Applicant Employment details
ministries = (
    ('Ministry of Education','Ministry of Education')
)
class EmploymentDetails(models.Model):
    applicant = models.OneToOneField(Applicant,on_delete=models.CASCADE,related_name='employment_details')
    employer_name = models.CharField(max_length=100)
    #employer_tel_no = models.IntegerField(null=True, blank=True)
    #employer_contact_person= models.CharField(max_length=100,null=True,blank=True)
    #employer_address= models.CharField(max_length=100,null=True,blank=True)
    employee_number = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    #date_joined = models.DateField()
    #expiry_of_employment = models.CharField(max_length=100)
    #gross_salary = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    #net_salary = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    
#applicant next of kin details
class NextOfKinDetails(models.Model):
    applicant = models.OneToOneField(Applicant,on_delete=models.CASCADE,related_name='next_of_kin_details')
    title = models.CharField(max_length=100,choices= titles)
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    #maiden_name = models.CharField(max_length=100,null=True,blank=True,default="N/A")
    #address = models.TextField()
    national_id_no = models.CharField(max_length=12)
    relationship = models.CharField(max_length=100)
    #employer = models.CharField(max_length=100,null=True,blank=True,default="N/A")
    #profession = models.CharField(max_length=100)
    contact_number = models.IntegerField()
    #dob= models.DateField()
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    image =  models.ImageField(upload_to="products/")
    
    def __str__(self):
        return self.name
#applicant loan details
loan_types = (
    ('Personal Loan','Personal Loan'),
    ('Other','Other')
)
disbursement_options=(
    ('Bank Account','Bank Account'),
    ('EcoCash','Eco Cash'),
    ('Others','Others')
)
has_loan_amount =(
    ('Yes','Yes'),('No','No')
)
loan_tenures = (
    ('3 months','3 months'),
    ('6 months','6 months'),
    ('12 months','12 months'),
    ('24 months','24 months')
)
class LoanDetails(models.Model):
    applicant = models.ForeignKey(Applicant,on_delete=models.CASCADE,related_name='loan_details')
    loan_type = models.CharField(max_length=100,choices=loan_types)
    loan_purpose = models.CharField(max_length=200,null=True,blank=True)
    product = models.ForeignKey(Product,on_delete=models.DO_NOTHING,related_name='product_loans',null=True,blank=True)
    disbursement_option = models.CharField(max_length=100,choices=disbursement_options)
    existing_loan_amount= models.CharField(max_length=100,choices=has_loan_amount)
    loan_amount = models.DecimalField(max_digits=10,decimal_places=2)
    loan_tenure = models.CharField(max_length=100,choices=loan_tenures)
    payslip = models.FileField(upload_to="files/payslip/",null=True,blank=True)
    national_id = models.FileField(upload_to='files/national_id/',null=True,blank=True)
    monthly_installment = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    has_confirmed = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    agent = models.ForeignKey(Agent,on_delete=models.CASCADE,related_name='agent_loans',null=True,blank=True)
    
# class Cession(models.Model):
#     applicant = models.OneToOneField(Applicant,on_delete=models.CASCADE,related_name='loan_cessions')


