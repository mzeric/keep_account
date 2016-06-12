from django.contrib import admin

# Register your models here.
from fei.models import *

from django.conf.locale.en import formats as en_formats
en_formats.DATETIME_FORMAT = "Y-m-d H:i:s"

def get_balance_with_total(ren, fan):
    pass
        

def get_balance_with_share(ren, fan, balance):
    all_sep = ChiFan_Sep.objects.filter(chifan = fan)
    all_sharing_ren = fan.ren.all()
    t_sep_sum = 0
    for sep in all_sep:
        if sep.ren == ren:
           balance = balance - sep.cost
           print "sep - ",sep.cost

    #t_share = t_total - t_sep_sum
    if ren in all_sharing_ren:
        t_sharing = fan.cost_sharing
        t_sep_share = t_sharing/len(all_sharing_ren)
        balance = balance - t_sep_share
        print "share - ", t_sep_share
    return balance

def get_balance_with_charge(ren, charge, balance):
    if ren == charge.ren:
        balance = balance + charge.money
        print "charge + ",charge.money
    
    return balance

def get_balance_with(ren):
    balance = 0
    for fan in ChiFan.objects.all():
        balance = get_balance_with_share(ren, fan, balance)
    for charge in Charge.objects.all():
        balance = get_balance_with_charge(ren, charge, balance)
    print ren,"balance = ",balance
    return balance
    

def get_share():
    if share != 0:
        return share
    if total == 0:
        return 0


def balance(modelAdmin, request, queryset):
    print modelAdmin,request,queryset

    for ren in queryset:
        ren.balance = get_balance_with(ren)
        print ren,"balance : ", ren.balance
        ren.save()


class RenAdmin(admin.ModelAdmin):
    list_display = ('name','balance')
    actions=[balance]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['name', 'balance']
        else:
            return []

class ChargeAdmin(admin.ModelAdmin):
    list_display = ('ren', 'money', 'date')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['ren', 'money']
        else:
            return []

class ChiFan_Sep_Inline(admin.StackedInline):
    model = ChiFan_Sep
    extra = 0
class ChiFanAdmin(admin.ModelAdmin):
    list_display = ('addr', 'date')
    inlines=[ChiFan_Sep_Inline]
    
    def get_readonly_fields(self, request, obj=None):
        return []


admin.site.register(ChiFan, ChiFanAdmin)
admin.site.register(Charge, ChargeAdmin)
admin.site.register(Ren, RenAdmin)
