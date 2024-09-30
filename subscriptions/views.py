from django.http import HttpResponse
from django.shortcuts import render
from subscriptions.forms import SubscriptionForm

def subscribe(request):
    context = {'form': SubscriptionForm()}
    return render(request, 'subscriptions/subscriptions_form.html', context)
