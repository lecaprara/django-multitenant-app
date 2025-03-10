from rest_framework import serializers
from django.core.exceptions import ValidationError
import re
from .models import Client, Domain

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['name', 'schema_name']

    def validate_schema_name(self, value):
        if not re.match(r'^[a-z0-9_]+$', value):
            raise serializers.ValidationError("O name do schema deve conter apenas letras minúsculas, números e underscores.")
        return value

class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = ["id", "domain", "tenant", "is_primary"]
