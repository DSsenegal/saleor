import graphene

from graphene_django import DjangoObjectType
from tenants.models import Client

from ..types import TenantType



class TenantCreate(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)
        adminEmail = graphene.String(required=True)
        adminPhone = graphene.String(required=True)
        domainUrl = graphene.String(required=True)

    # The class attributes define the response of the mutation
    tenant = graphene.Field(TenantType)

    @classmethod
    def mutate(cls, root, info, id, name, adminEmail, adminPhone, domainUrl):
        schema_name = name.replace(" ", "_")
        tenant = Client(
            name = name,
            paid_until =  "2026-01-01",
            schema_name = schema_name,
            admin_phone = adminPhone,
            admin_email = adminEmail,
            domain_url = domainUrl,
        )
        tenant.save()
        # Notice we return an instance of this mutation
        return TenantCreate(tenant=tenant)