from django.shortcuts import render
from asgiref.sync import sync_to_async
from .models import Manufacturer, Product
import asyncio


async def product_list_view(request):
    get_products = sync_to_async(
        lambda: list(Product.objects.select_related('manufacturer_id').all())
    )
    get_manufacturers = sync_to_async(
        lambda: list(Manufacturer.objects.all())
    )

    products, manufacturers = await asyncio.gather(
        get_products(),
        get_manufacturers()
    )

    return render(request, 'index.html', {
        'products': products,
        'manufacturers': manufacturers
    })