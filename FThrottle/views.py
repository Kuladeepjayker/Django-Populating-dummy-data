# Create your views here.
from rest_framework import viewsets
from .serializers import MembersSerializer
from .models import Members


class MembersViewSet(viewsets.ModelViewSet):
    queryset = Members.objects.all().order_by('name')
    serializer_class = MembersSerializer
