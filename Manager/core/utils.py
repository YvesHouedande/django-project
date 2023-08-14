from .models import Product

def find_products(sessionProducts, kind):
    products = []
    for key in sessionProducts.keys():
        try:
            product = Product.objects.get(id=int(key), kind=kind) 
            products.append({"id":product.id, "name":product.name,
                            'kind':product.kind, 'ref':product.reference,
                            "qte":sessionProducts[key]})
        except:
            pass
    return products


from .models import Order, LigneOrder

def update_stock_on_validation(order):
    for ligne_order in order.ligneorder_set.all():
        product = ligne_order.product
        product.quantity -= ligne_order.quantite
        product.save()

def context_total_cart(request):
    cart_total = sum([int(key) for key in request.session.get("cart", {}).values() ])
    return {"cart_total": cart_total}