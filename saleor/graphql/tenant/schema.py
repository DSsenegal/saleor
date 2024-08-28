import graphene
from tenant.models import Client
from graphene_django import DjangoObjectType


class TenantType(DjangoObjectType):
    class Meta:
        model = Client
        fields = ("id", "name", "description", "domain_url", "admin_email", "admin_phone", "is_approved")
        

class TenantQueries(graphene.ObjectType):
    tenants = graphene.List(TenantType)
    tenant = graphene.Field(TenantType, id=graphene.String())
    
    def resolve_tenants(self, info):
        return Client.objects.all()
    
    def resolve_tenant(self, info, id):
        return Client.objects.get(pk=id)

schema = graphene.Schema(query=TenantQueries)