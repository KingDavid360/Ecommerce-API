from rest_framework import serializers
from .models import MerchantProfile

class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = MerchantProfile
        fields = "__all__"
