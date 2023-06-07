from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Transaction,Loan,Response
# Register your models here.


admin.site.site_header ='MASASE ENTERPRISE APPLICATION'
admin.site.site_title ='MASASE | ERP'
admin.site.index_title ='MASASE ENTERPRISE APPLICATION'


@admin.register(Transaction)
class TransactionAdmin(ImportExportModelAdmin):
    list_display = ('title','forename','surname','bank','phone_number')
    #list_filter =('assigned',)
    search_fields =('forename','surname',)
    list_max_show_all =40
    
    
@admin.register(Loan)
class CustomerInformationAdmin(ImportExportModelAdmin):
    list_display = ('loan_reference','title','forenames','surname','bank','phone_no','ecno','loan_status')
    list_filter =('loan_status',)
    search_fields =('forenames','surname','ecno','loan_reference',)
    list_max_show_all =50
    
@admin.register(Response)
class ResponseAdmin(ImportExportModelAdmin):
    list_display = ('reference','ecnumber','status','message')
    list_filter =('status',)
    search_fields =('reference','ecnumber',)
    list_max_show_all =50

