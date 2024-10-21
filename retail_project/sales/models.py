from django.db import models

class SalesSummary(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    total_sales = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False  # This tells Django that this is an existing table not managed by Django
        db_table = 'v_sales_summary'  # Ensure this matches the exact name of your view in the database
