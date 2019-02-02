from django.shortcuts import get_object_or_404 ,render
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger,Paginator
from listings.reduce import bedroom_choices,price_choices,state_choices
def index(request):
    listings =Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator=Paginator(listings,6)
    page=request.GET.get('page')
    paged_listings=paginator.get_page(page)
    context ={
        'listings':paged_listings

    }

    return render(request,'listings/listings.html',context)

def listing(request,listing_id):
    listing=get_object_or_404(Listing,pk=listing_id)
    context ={
        'listing':listing

    }
    return render(request,'listings/listing.html',context)

def search(request):
    listing=Listing.objects.all().order_by('-list_date')

    #keywords
    if 'keywords' in request.GET:
        keywords=request.GET['keywords']
        if keywords:
            listing=listing.filter(description__icontains=keywords)
    # city
    if 'city' in request.GET:
        city=request.GET['city']
        if city:
            listing=listing.filter(city__iexact=city)      
    # state
    if 'state' in request.GET:
        state=request.GET['state']
        if state:
            listing=listing.filter(state__iexact=state)     
    # price
    if 'price' in request.GET:
        price=request.GET['price']
        if price:
            listing=listing.filter(price__lte=price)     
    # bedrooms
    if 'bedrooms' in request.GET:
        bedrooms=request.GET['bedrooms']
        if bedrooms:
            listing=listing.filter(bedrooms__lte=bedrooms)

    context={
        'listing':listing,
        'values':request.GET,
        'price_choices':price_choices,
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
    }
    return render(request,'listings/search.html',context)