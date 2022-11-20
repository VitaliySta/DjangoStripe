import stripe

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView

from items.models import Item
from TaskStrip.settings import STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY

from .serializers import ItemSerializer

DOMAIN = "http://127.0.0.1:8000/"
stripe.api_key = STRIPE_SECRET_KEY


class ItemDetailView(APIView):

    def get(self, request, id):
        item = get_object_or_404(Item, id=id)
        serializer = ItemSerializer(item)
        context = {
            'item': serializer.data,
            'stripe_public_key': STRIPE_PUBLIC_KEY
        }
        return render(request, 'items/index.html', context=context)


class BuyView(APIView):

    def get(self, request, id):
        item = get_object_or_404(Item, id=id)
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': item.price,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=DOMAIN + 'success/',
            cancel_url=DOMAIN + 'cancel/',
        )
        return JsonResponse({'id': checkout_session.id})
