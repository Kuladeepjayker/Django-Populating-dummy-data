from rest_framework import serializers

from .models import Members

class MembersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Members
        fields = ('id', 'name', 'alias', 'date')
