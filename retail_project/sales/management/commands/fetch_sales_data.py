from django.core.management.base import BaseCommand
from django.db import connection
from sales.models import SalesSummary

class Command(BaseCommand):
    help = 'Fetches sales data from the PostgreSQL view and stores it in Django'

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM v_sales_summary')
            rows = cursor.fetchall()

            for row in rows:
                SalesSummary.objects.update_or_create(
                    product_name=row[0],
                    category=row[1],
                    defaults={'total_sales': row[2]}
                )
