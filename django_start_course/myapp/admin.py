from django.contrib import admin
from django.contrib.admin.models import LogEntry, CHANGE
from django.contrib.contenttypes.models import ContentType

from .models import Article, Account

# Register your models first

# admin.site.register(Account)
admin.site.register(Article)

# ContentType.objects.get_for_model(Account)


# class CustomLogEntryAdmin(admin.ModelAdmin):
#     list_display = ['__str__', 'action_time', 'user', 'content_type', 'object_id', 'object_repr', 'action_flag']

# admin.site.register(LogEntry, CustomLogEntryAdmin)
