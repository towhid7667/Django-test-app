import json

from django.http import JsonResponse

from products.models import Product
from django.forms.models import model_to_dict


def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price
        data = model_to_dict(model_data, fields=['id', 'title'])

    return JsonResponse(data)
