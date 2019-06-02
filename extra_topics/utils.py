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

def get_categories_info(categories_qs, active_subcategories=False):
    categories = []
    for category in categories_qs:
        if active_subcategories:
            subcategories = [sub.name for sub in category.sub_categories.filter(is_active=True)]
        else:
            subcategories = [sub.name for sub in category.sub_categories.all()]
        categories.append({
            'name': category.name,
            'is_active': category.is_active,
            'subcategories': subcategories
        })
    return categories


def list_products():
    products_qs = Product.objects.all()
    products = get_products_info(products_qs)
    return products

def list_products_with_select_related():
    products_qs = Product.objects.select_related('category').all()
    products = get_products_info(products_qs)
    return products

def list_categories():
    categories_qs = Category.objects.all()
    categories = get_categories_info(categories_qs)
    return categories

def list_categories_with_prefetch_related():
    categories_qs = Category.objects.prefetch_related('sub_categories').all()
    categories = get_categories_info(categories_qs)
    return categories

def categories_list_active_subcategories():
    """Return all categories and list only the active subcatories."""
    categories_qs = Category.objects.prefetch_related("sub_categories")
    categories = get_categories_info(categories_qs, active_subcategories=True)