from django.db import models
from tenant_schemas.models import TenantMixin
from django.utils.timezone import now

class Client(TenantMixin):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, default=None, blank=True, null=True)
    paid_until =  models.DateField()
    on_trial = models.BooleanField(default=False)
    created_at = models.DateField(default=now, editable=False)
    admin_phone = models.CharField(max_length=25, default=None, blank=True, null=True)
    admin_email = models.CharField(max_length=64, default=None, blank=True, null=True)
    is_approved = models.BooleanField(default=False)

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True

class Draft(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, default=None, blank=True, null=True)
    admin_phone = models.CharField(max_length=25, default=None, blank=True, null=True)
    admin_email = models.CharField(max_length=64, default=None, blank=True, null=True)
    domain_url = models.CharField(max_length=64, default=None, blank=True, null=True)