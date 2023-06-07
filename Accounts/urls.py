from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('',home_page,name='homepage'),
    path('client/auth/',client_account_creation,name='create_student_account'),
    path('agent/auth/',agent_account_creation,name='create_agent_account'),
    path('auth/', auth_views.LoginView.as_view(template_name='auth/login.html',form_class=LoginForm), name='login'),
    # path('auth/agent/', auth_views.LoginView.as_view(template_name='auth/agent/login.html',form_class=LoginForm), name='agent_login'),
    # path('auth/staff/', auth_views.LoginView.as_view(template_name='auth/staff/login.html',form_class=LoginForm), name='staff_login'),
    path('profile/check/',profile_check,name="profile"),
    # path('student/profile/',student_dashboard,name="student_profile"),
    # path('teacher/profile/',teacher_dashboard,name="teacher_profile"),
    # path('admins/dashboard/',admin_dashboard,name="admin_dashboard"),
]
