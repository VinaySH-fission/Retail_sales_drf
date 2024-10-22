from django.core.management.base import BaseCommand
from django.db import connection
from sales.models import SalesSummary

class Command(BaseCommand):
    # This string describes the purpose of the command
    # which will appear in the 'manage.py help' output.
    help = 'Fetches sales data from the PostgreSQL view and stores it in Django'

    def handle(self, *args, **options):
        # Create a database cursor to execute SQL commands
        with connection.cursor() as cursor:
            # Execute an SQL query to select all records from the 'v_sales_summary' view
            cursor.execute('SELECT * FROM v_sales_summary')
            # Fetch all the rows returned by the SQL query
            rows = cursor.fetchall()

            # Loop through each row in the results
            for row in rows:
                """For each row, update or create a SalesSummary object in Django's database
                'update_or_create' tries to find a SalesSummary object with a matching
                product_name and category. If it exists, it updates it with the new total_sales.
                If it doesn't exist, it creates a new object with the provided fields."""
                SalesSummary.objects.update_or_create(
                    product_name=row[0],  # Name of the product
                    category=row[1],      # Category of the product
                    defaults={'total_sales': row[2]}  # Dictionary specifying fields to update
                )
