from django.shortcuts import render,  get_object_or_404,redirect
from .models import Order, ProfileUtisateur, Product, Category, LigneOrder
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


def profiles_list(request):
    profileUtisateurs = ProfileUtisateur.objects.all()
    return render(request, 'index.html', {'profileUtisateurs': profileUtisateurs})

@login_required
def product_list(request):
    categories = Category.objects.all()
    nb_categories = Category.objects.count()
    nb_per_col = (nb_categories + 3) // 4  
    products = Product.objects.all()
    nb = [Category.objects.count(), Product.objects.count()]

    paginator = Paginator(products, 12) 
    page_number = request.GET.get('page')  
    products_page = paginator.get_page(page_number)
    
    if categories:
        categories_grouped = [categories[i:i+nb_per_col] for i in range(0, nb_categories, nb_per_col)]
    else:
        categories_grouped= []
    context = {
        'products': products,
        'categories_grouped': categories_grouped,
        'nb':nb,
        # "cart_total":cart_total
        'products_page':products_page
               }
    return render(request, 'index.html', context)

@login_required
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order_detail.html', {'order': order})



def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirigez l'utilisateur vers la page souhaitée après la connexion
                return redirect('product_list')
            else:
                messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    else:
        form = LoginForm()

    return render(request, 'connexion.html', {'form': form})

@login_required
def filter_products(request, kind=None, category_name=None):
    cats = Category.objects.all()
    keyword = request.GET.get('search', '')
    products = Product.objects.all()
    if keyword:
        products = products.filter(name__icontains=keyword)
    if kind:
        products = products.filter(kind=kind)
    if category_name:
        products = products.filter(category__nom=category_name)

    paginator = Paginator(products, 3)
    page_number = request.GET.get('page')  
    products_page = paginator.get_page(page_number)     
    context = {

        'products': products,
        "products_page":products_page,
        'kind': kind,
    }

    return render(request, 'filter_products.html', context)

@login_required
def add_to_cart(request):
    if request.method == 'GET':
        if request.path.startswith("/add_to_cart/") and int(request.GET.get('quantity'))>0 :
            product_id = request.GET.get('product_id')
            quantity = request.GET.get('quantity') 
            cart = request.session.get("cart", {})
            cart[product_id] = quantity
        elif request.path.startswith("/restaure/"):
            product_id = request.GET.get('product_id')
            cart = request.session.get("cart", {})
            cart.pop(product_id)
        request.session['cart'] = cart
        cart_total = sum([int(key) for key in request.session.get("cart", {}).values() ])
        data = {"cart_total": cart_total}
        return JsonResponse(data, safe=False)
    else:
        return HttpResponse("Cette route ne prend en charge que les requêtes POST.")


from .utils import find_products
@login_required
def listPanier(request):
    int_products = find_products(request.session.get("cart",{}), "Intrant")
    sort_products = find_products(request.session.get("cart",{}), "Sortie")
    out_products = find_products(request.session.get("cart",{}), 'Outils') 
    Ent_products = find_products(request.session.get("cart",{}), 'Entree')

    context = {
        'int_products':int_products,
        'sort_products':sort_products,
        "out_products":out_products,
        "Ent_products":Ent_products
    }
    return render(request, "order.html", context)

@login_required
def handle_order(request):
    profile = get_object_or_404(ProfileUtisateur, user=request.user)
    order = Order.objects.create(client=profile)
    cart_items = request.session.get("cart", {})
    for key, value in cart_items.items():
        LigneOrder.objects.create(commande=order, product_id=int(key),
        quantite=int(value))

    request.session["cart"]= {}
    return redirect('product_list')

