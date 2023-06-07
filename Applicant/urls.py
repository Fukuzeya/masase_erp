from django.urls import path
from .views import *



app_name = 'applicant'

urlpatterns =[
    path('profile/',client_profile,name='client_profile'),
    path('products/',get_available_products,name='available_products'),
    path('loan/confirmed/',confirm_loan,name='confirm_loan'),
    path('loans/',get_my_loans,name='applied_loans'),
    path('loan/application/<int:id>/',loan_application,name='loan_application'),
    path('application/stage_5/',application_process_five, name='app_process_five'),
    path('application/stage_4/',application_process_four, name='app_process_four'),
    path('application/stage_3/',application_process_three, name='app_process_three'),
    path('application/stage_2/',application_process_two, name='app_process_two'),
    path('application/stage_1/',application_process_one, name='app_process_one'),
]