from django.db import models


class AuditFieldMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SoftDeleteMixin(models.Model):
    is_active = models.BooleanField(default=True)
    is_hidden = models.BooleanField(default=False)

    class Meta:
        abstract = True