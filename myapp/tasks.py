from celery import shared_task
from .models import Product
from .utils import categorize_product

@shared_task
def categorize_product_task(product_id):
    try:
        product = Product.objects.get(id=product_id)
        product.category = categorize_product(product.title, product.description)
        product.save()
    except Product.DoesNotExist:
        pass
