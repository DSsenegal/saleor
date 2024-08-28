import graphene
from tenant.models import Client, Draft
from .types import TenantType, TenantDraftType
from .mutations.tenant_create import TenantCreate
from .mutations.tenant_draft_create import TenantDraftCreate
from .mutations.tenant_approve import TenantApprove

class TenantQueries(graphene.ObjectType):
    tenants = graphene.List(TenantType)
    tenants_draft = graphene.List(TenantDraftType)
    tenant = graphene.Field(TenantType, id=graphene.String())
    
    def resolve_tenants(self, info):
        return Client.objects.all()
    
    def resolve_tenant(self, info, id):
        return Client.objects.get(pk=id)

    def resolve_tenants_draft(self, info):
        return Draft.objects.all()
    
class TenantMutations(graphene.ObjectType):
    tenant_create = TenantCreate.Field()
    tenant_draft_create = TenantDraftCreate.Field()
    tenant_approve = TenantApprove.Field()
    
schema = graphene.Schema(query=TenantQueries, mutation=TenantMutations)