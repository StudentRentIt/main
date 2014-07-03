from django.shortcuts import render

import stripe

# Create your views here.

def payment(request):
    token = ""
    message = ""

    if request.method == "POST":

        # Set your secret key: remember to change this to your live secret key in production
        # See your keys here https://manage.stripe.com/account
        stripe.api_key = "sk_test_BU1tsOK2ERirE6WsvDHfYCwt"

        # Get the credit card details submitted by the form
        token = request.POST['stripeToken']

        # Create the charge on Stripe's servers - this will charge the user's card
        try:
          charge = stripe.Charge.create(
              amount=1000, # amount in cents, again
              currency="usd",
              card=token,
              description="payinguser@example.com"
          )
        except stripe.CardError as e:
          # The card has been declined
          ""
          message = "declined :("

    return render(request, 'payments/content/payment.html',
        {'token':token, 'message':message})