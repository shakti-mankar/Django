from django.shortcuts import render
from .models import Product

# Create your views here.

def landing(req):
    return render(req,"landing.html")


def form(req):
    if req.method == "POST":
        name = req.session.get("name")
        category = req.session.get("category")
        price = req.session.get("price")
        quantity = req.session.get("quantity")
        brand = req.session.get("brand")
        description = req.session.get("desc")


        Product.objects.create(
            name=name,
            category=category,
            price=price,
            quantity=quantity,
            brand=brand,
            description=description
        )

        return redirect("showproduct")

    return render(req,"form.html")


def showproduct(req):
    return render(req,"showproduct.html")