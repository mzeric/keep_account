from django.contrib import admin

# Register your models here.
from fei.models import *

class RenAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(ChiFan)
admin.site.register(Charge)
admin.site.register(Ren, RenAdmin)
