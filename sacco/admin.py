from django.contrib import admin

from sacco.models import Customer, Deposit

# Register your models here.

admin.site_header = 'Rongai Sacco Administration'
admin.site.site_title = ' Sacco Admin'

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name',
                    'last_name',
                    'email',
                    'gender',
                    'dob']
    search_fields = ['first_name',
                    'last_name',
                    'email']
    list_filter = ['gender']
    list_per_page = 20

class DepositAdmin(admin.ModelAdmin):
    list_display = ['customer',
                    'created_at',
                    'amount',
                    'status']
    search_fields = ['customer',
                     'status',
                     'amount']
    list_per_page = 20
    list_filter = ['status']

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Deposit, DepositAdmin)



#python manage.py --help

# python manage.py createsuperuser
# admin@gmail.com
# 123456

# localhost:8000/admin

# 1a2Bc9*33aa!!