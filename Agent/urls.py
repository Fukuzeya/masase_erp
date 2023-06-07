from django.urls import path
from .views import *



app_name = 'agent'

urlpatterns =[
    path('',agent_profile,name='agent_profile'),
    path('application/stage-1/',application_process_one,name='stage_1'),
    path('application/stage-2/',application_process_two,name='stage_two'),
    path('application/stage-3/',application_process_three,name='stage_three'),
    path('application/stage-4/',application_process_four,name='stage_four'),
    path('application/stage-5/',application_process_five,name='stage_five'),
    
]