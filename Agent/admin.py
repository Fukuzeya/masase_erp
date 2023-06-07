from django.contrib import admin

from .models import Agent
# Register your models here.


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','gender','phone_number','city','join_date')
    list_filter =('first_name','gender','city',)
    search_fields =('first_name','last_name',)
    list_max_show_all =40
