# from django.http import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render
from .models import Shop, Product, Deal


# Create your views here.
def index(req):
    shops = Shop.objects.all()
    products = Product.objects.all()
    deals = Deal.objects.all()
    context = {
        "shops": shops,
        "products": products,
        "deals": deals,
    }
    return render(req, "myapp/index.html", context)


def test(request):
    return HttpResponse("Test Page")

# from shop.models import Event
#
#
# def index(request):
#     event_list = Event.objects.all()
#     context = {
#         'events': event_list
#     }
#     return render(request, 'shop/registration/index.html', context)
#
#     # return HttpResponse("Hello world")
#
#
