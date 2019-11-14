from django.contrib import admin
from .models import Payment


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount', 'amount_paid', 'create_date', 'update_date')


admin.site.register(Payment, PaymentAdmin)