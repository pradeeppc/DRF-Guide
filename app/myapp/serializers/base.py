from rest_framework import serializers

class BaseSerializer(serializers.Serializer):

    class Meta:
        fields = [
            'created_on',
            'modified_on',
            'deleted_on',
        ]
