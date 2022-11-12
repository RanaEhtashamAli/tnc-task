from django.contrib import admin
from .models import ExchangeRate

@admin.register(ExchangeRate)
class ExchangeRateAdmin(admin.ModelAdmin):
    list_display = ('from_currency_code', 'to_currency_code', 'exchange_rate', 'last_refreshed')
    list_filter = ('is_active', 'is_hidden')
