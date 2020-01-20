from django.utils import timezone
from .... import *


def create_product(info, data):
    product = Product(categoryid=Category.objects.get(pk=data.get("categoryid")),
                      title=data.get("title"),
                      description=data.get("description", None),
                      userid=AuthUser.objects.get(pk=info.context.user.id),
                      created=timezone.now())
    product.save()
    return product


def update_product(data):
    product = Product.objects.get(pk=data.get("productid"))
    product.categoryid = Category.objects.get(pk=data.get("categoryid"))
    product.title = data.get("title")
    product.description = data.get("description", None)

    product.save()
    return product


def create_productdetails(info, data):
    productdetails = Productdetails(productid=Product.objects.get(pk=data.get("productid")),
                                    model=data.get("model", None),
                                    url=data.get("url", None),
                                    weight=data.get("weight", 0.0),
                                    height=data.get("height", 0.0),
                                    width=data.get("width", 0.0),
                                    lenght=data.get("lenght", 0.0),
                                    userid=AuthUser.objects.get(pk=info.context.user.id),
                                    created=timezone.now())
    productdetails.save()
    return productdetails


def create_debit(info, data):
    debit = Debit(warehouseid=Warehouse.objects.get(pk=data.get("warehouseid")),
                  productid=Product.objects.get(pk=data.get("productid")),
                  qty=data.get("qty", 0.00),
                  price=data.get("price", 0.00),
                  pricetypeid=Pricetype.objects.get(pk=data.get("pricetypeid")),
                  discountid=Discount.objects.get(pk=data.get("discountid")),
                  statusid=Status.objects.get(pk=data.get("statusid")),
                  notes=data.get("notes", None),
                  userid=AuthUser.objects.get(pk=info.context.user.id),
                  created=timezone.now())

    debit.save()
    return debit
