from rest_framework import serializers
from sales.models import SalesSummary

class SalesSummarySerializer(serializers.ModelSerializer):
    """
    Serializer for SalesSummary model.

    This serializer converts instances of the SalesSummary model into JSON format
    and validates incoming data used to create or update SalesSummary instances.
    """

    class Meta:
        """
        Meta subclass to define serializer behavior.
        """
        # Specifies the model associated with this serializer.
        model = SalesSummary
        
        # Specifies the model fields that should be included in the serialized output.
        # This list also defines which fields can be accepted when creating or updating an instance
        # via the serializer, assuming no read_only settings are applied.
        fields = ['product_name', 'category', 'total_sales']
