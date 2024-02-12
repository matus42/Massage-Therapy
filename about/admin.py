from django.contrib import admin
from .models import AboutPage
from django_summernote.admin import SummernoteModelAdmin


class AboutPageAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)


admin.site.register(AboutPage, AboutPageAdmin)
# Register your models here.
