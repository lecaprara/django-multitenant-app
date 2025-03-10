from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from .models import User
from django.shortcuts import redirect
from django.http import Http404
from django_tenants.utils import tenant_context
from clients.models import Client

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return User.objects.all()
        return User.objects.filter(client=user.profile.client)

def set_client(request):
    client_name = request.GET.get('client')
    if not client_name:
        raise Http404("Client not specified.")

    try:
        client = Client.objects.get(name=client_name)
    except Client.DoesNotExist:
        raise Http404("Client not found.")

    with tenant_context(client):
        request.session['client'] = client.name

    return redirect(f"/login")