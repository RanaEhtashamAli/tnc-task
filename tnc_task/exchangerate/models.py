from django.db import models
from tnc_task.core.models import AuditFieldMixin, SoftDeleteMixin


class ExchangeRate(AuditFieldMixin, SoftDeleteMixin):
    from_currency_code = models.CharField(max_length=3)
    from_currency_name = models.CharField(max_length=50)
    to_currency_code = models.CharField(max_length=3)
    to_currency_name = models.CharField(max_length=50)
    exchange_rate = models.DecimalField(max_digits=14, decimal_places=8)
    last_refreshed = models.DateTimeField()
    time_zone = models.CharField(max_length=25)
    bid_price = models.DecimalField(max_digits=14, decimal_places=8)
    ask_price = models.DecimalField(max_digits=14, decimal_places=8)

    def __str__(self):
        return f'{self.exchange_rate} - {self.last_refreshed}'
