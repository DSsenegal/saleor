from django.db import connections
from django_tenants.middleware import TenantMainMiddleware
from django_tenants.utils import get_tenant_domain_model


class CustomTenantMiddleware(TenantMainMiddleware):
    def process_request(self, request):
        # Connection needs first to be at the public schema, as this is where
        # the tenant metadata is stored.
    
        for con in connections:
            connections[con].cursor().execute("SET search_path to public")
        
        
        hostname = self.hostname_from_request(request)
        domain_model = get_tenant_domain_model()
        tenant = self.get_tenant(domain_model, hostname)
    
        
        for con in connections:
            connections[con].cursor().execute("SET search_path to %s" % tenant.schema_name)
    
        # routing to the