from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    #validate prix field
    def validate_prix(self, value):
        if value <= 0:
            raise serializers.ValidationError("le prix doit être positive")
        return value

    #validate stock field
    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("Le stock doit être supérieur ou égal à 0.")
        return value
