from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Accounts.urls',namespace='accounts')),
    path('management/',include('Management.urls',namespace='management')),
    path('applicant/',include('Applicant.urls',namespace='applicant')),
    path('agent/',include('Agent.urls',namespace='agent')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

