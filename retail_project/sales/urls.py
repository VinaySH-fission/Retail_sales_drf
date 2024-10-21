from django.urls import path
from .views import SalesData

urlpatterns = [
    path('sales/', SalesData.as_view(), name='sales-data'),
]
