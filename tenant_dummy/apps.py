from django.apps import AppConfig


class TenantDummyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tenant_dummy'
