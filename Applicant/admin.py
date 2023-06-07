from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Product)
admin.site.register(LoanDetails)
admin.site.register(Applicant)
admin.site.register(EmploymentDetails)