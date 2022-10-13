from email.policy import default
from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """_summary_

    Args:
        serializers (_type_): _product serializer with user hidden field_
    """
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Product
        fields = '__all__'