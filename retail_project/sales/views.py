from rest_framework.views import APIView
from rest_framework.response import Response
from sales.models import SalesSummary
from sales.serializers import SalesSummarySerializer

class SalesData(APIView):
    def get(self, request):
        data = SalesSummary.objects.all()
        serializer = SalesSummarySerializer(data, many=True)
        return Response(serializer.data)
