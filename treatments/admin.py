from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Massage

# Register your models here.


class MassageAdmin(SummernoteModelAdmin):
    summernote_fields = ('description', 'details')


admin.site.register(Massage, MassageAdmin)
