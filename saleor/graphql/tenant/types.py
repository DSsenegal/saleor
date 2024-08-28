from tenant.models import Client, Draft
from graphene_django import DjangoObjectType


class TenantType(DjangoObjectType):
    class Meta:
        model = Client
        fields = ("id", "name", "description", "domain_url", "admin_email", "admin_phone", "is_approved")
        
class TenantDraftType(DjangoObjectType):
    class Meta:
        model = Draft
        fields = "__all__"