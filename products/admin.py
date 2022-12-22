from django.contrib import admin
from products.models import paymentmaking , info

# Register your models here.
class paymentmakingadmin(admin.ModelAdmin):
    list_display = ('id','name','phone_number','age')


admin.site.register(paymentmaking)
admin.site.register(info)

class info(admin.ModelAdmin):
    list_display = ('fullname','mobile_number',)