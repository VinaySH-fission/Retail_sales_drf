from rest_framework.views import APIView
from rest_framework.response import Response
from sales.models import SalesSummary
from sales.serializers import SalesSummarySerializer

class SalesData(APIView):
    """
    API view to retrieve sales data.

    Extends Django REST Framework's APIView to create a read-only endpoint
    that provides access to sales data.
    """
    
    def get(self, request):
        """
        Handle GET requests to the SalesData API endpoint.

        This method retrieves all entries in the SalesSummary model, serializes them,
        and returns them in a JSON format.

        Args:
            request (HttpRequest): The request object used to generate the response.

        Returns:
            Response: Django REST Framework response object containing serialized sales data.
        """
        # Retrieve all objects from the SalesSummary model.
        data = SalesSummary.objects.all()
        
        # Serialize the data. The 'many=True' flag indicates that we are serializing
        # a queryset (multiple objects) rather than a single object instance.
        serializer = SalesSummarySerializer(data, many=True)
        
        # Return a Response object containing the serialized data. By default,
        # Django REST Framework converts the Python data types to JSON.
        return Response(serializer.data)
