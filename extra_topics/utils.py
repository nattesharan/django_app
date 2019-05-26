from extra_topics.models import Product, Category

def get_products_info(products_qs):
    products = []
    for product in products_qs:
        products.append({
            'id': product.id,
            'title': product.title,
            'category': product.category.name
        })
    return products

def list_products():
    products_qs = Product.objects.all()
    products = get_products_info(products_qs)
    return products

def list_products_with_select_related():
    products_qs = Product.objects.select_related('category').all()
    products = get_products_info(products_qs)
    return products

