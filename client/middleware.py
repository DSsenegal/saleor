from django.db import connections
from django_tenants.middleware import TenantMainMiddleware
from django_tenants.utils import get_tenant_domain_model, get_public_schema_name, get_tenant_model

class CustomTenantMainMiddleware(TenantMainMiddleware):
    # def get_tenant(self, hostname, request):
    #     tenant = super().get_tenant(hostname, request)
    #     print("Custom tenant ",tenant)
    #     return tenant

    def process_request(self, request):
        print("*** Custom tenant main middleware ***")
        hostname = self.hostname_from_request(request)
        
        domain_model = get_tenant_domain_model()
        tenant = self.get_tenant(domain_model, hostname)
        
    
        
        for con in connections:
            connections[con].cursor().execute(f"SET search_path TO {tenant.schema_name}")
            
        self.setup_url_routing(request)