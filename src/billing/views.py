from django.shortcuts import render

import stripe
stripe.api_key = 'sk_test_08ucz8tyzZrXI1bR5ky7k6HM00FDKFrObZ'
STRIPE_PUB_KEY = 'pk_test_4JSoCm7Hyt6uEgMipMwGVFd900wH8BDxo0'

def payment_method_view(request):
    if request.method == "POST":
        print(request.POST)
    return render(request, 'billings/payment-method.html', {"publish_key": STRIPE_PUB_KEY})
