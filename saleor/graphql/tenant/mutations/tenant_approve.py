import graphene

from graphene_django import DjangoObjectType
from tenant.models import Client, Draft

from ..types import TenantType



class TenantApprove(graphene.Mutation):
    class Arguments:
        domainUrl = graphene.String(required=True)

    # The class attributes define the response of the mutation
    tenant = graphene.Field(TenantType)

    @classmethod
    def mutate(cls, root, info, domainUrl):
        draft = Draft.objects.get(domain_url=domainUrl)
        tenant = Client(
            name = draft.name,
            paid_until =  "2026-01-01",
            schema_name = draft.name.replace(" ", "_"),
            admin_phone = draft.admin_phone,
            admin_email = draft.admin_email,
            domain_url = draft.domain_url,
            is_approved = True
        )
        
        tenant.save()
        
        # Notice we return an instance of this mutation
        return TenantApprove(tenant=tenant)