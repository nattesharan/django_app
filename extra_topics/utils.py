from extra_topics.models import Product, Category

def list_products():
    products_qs = Product.objects.all()
    products = []
    for product in products_qs:
        products.append({
            'id': product.id,
            'title': product.title,
            'category': product.category.name
        })
    return products

