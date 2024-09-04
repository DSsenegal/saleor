from tenants.models import Client, Domain, Draft
from graphene_django import DjangoObjectType
from graphene import String


class TenantType(DjangoObjectType):
    domain = String()
    class Meta:
        model = Client
        fields = ("id", "name", "description", "domain", "admin_email", "admin_phone", "is_approved")
    
    def resolve_domain(self, info):
        domain = Domain.objects.filter(tenant=self).first()
        return domain.domain if domain else None
    
class TenantDraftType(DjangoObjectType):
    class Meta:
        model = Draft
        fields = "__all__"