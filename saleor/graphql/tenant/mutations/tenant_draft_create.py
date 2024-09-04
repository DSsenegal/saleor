import graphene

from graphene_django import DjangoObjectType
from tenants.models import Client, Draft

from ..types import TenantDraftType



class TenantDraftCreate(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String()
        adminEmail = graphene.String(required=True)
        adminPhone = graphene.String(required=True)
        domainUrl = graphene.String(required=True)

    # The class attributes define the response of the mutation
    tenant = graphene.Field(TenantDraftType)

    @classmethod
    def mutate(cls, root, info, name, description, adminEmail, adminPhone, domainUrl):
        schema_name = name.replace(" ", "_")
        tenant = Draft(
            name = name,
            description = description,
            admin_phone = adminPhone,
            admin_email = adminEmail,
            domain_url = domainUrl,
        )
        tenant.save()
        # Notice we return an instance of this mutation
        return TenantDraftCreate(tenant=tenant)