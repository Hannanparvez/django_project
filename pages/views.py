from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.reduce import price_choices,bedroom_choices,state_choices


def index(request):
    listings =Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context={
        'listings':listings,
        'price_choices':price_choices,
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
    }

    return render(request,'pages/index.html',context)

def about(request):
    realtors =Realtor.objects.all()
    mvps=Realtor.objects.filter(is_mvp=True)
    context={
        'realtors':realtors,
        'mvps':mvps
    }
    return render(request,'pages/about.html',context)

