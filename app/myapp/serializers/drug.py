from .base import BaseSerializer

from rest_framework import serializers
from myapp.models import Drug


class DrugSerializer(BaseSerializer, serializers.ModelSerializer):

    class Meta:
        model = Drug
        fields = BaseSerializer.Meta.fields + [
            'id',
            'sku_id',
            'product_id',
            'sku_name',
            'price',
            'manufacturer',
            'salt_name',
            'drug_form',
            'pack_size',
            'strength',
            'is_banned',
            'unit',
            'price_per_unit',
        ]
