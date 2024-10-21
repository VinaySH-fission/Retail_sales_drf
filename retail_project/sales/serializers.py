from rest_framework import serializers
from sales.models import SalesSummary

class SalesSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesSummary
        fields = ['product_name', 'category', 'total_sales']
