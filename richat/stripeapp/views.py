import stripe
import os

from django.shortcuts import render
from django.http import JsonResponse
from stripeapp.models import Item
from dotenv import load_dotenv

load_dotenv()

stripe.api_key = os.getenv('stripe.api_key')

# View для получения Stripe Session Id
def buy_item(request, id):
    item = Item.objects.get(id=id)
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
          "price_data": {
            "currency": "usd",
            "product_data": {
              "name": item.name,
            },
            "unit_amount": int(item.price * 100),
          },
          "quantity": 1,
        }],
        mode="payment",
        success_url=request.build_absolute_uri('/success/'),
        cancel_url=request.build_absolute_uri('/cancel/'),
    )
    return JsonResponse({'session_id': session.id})

# View для отображения информации о товаре
def item_detail(request, id):
    item = Item.objects.get(id=id)
    stripe_public_key = os.getenv('stripe_public_key')
    context = {'item': item, 'stripe_public_key': stripe_public_key}
    return render(request, "item_detail.html", context)

