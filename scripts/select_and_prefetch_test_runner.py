from extra_topics.utils import list_products

def run():
    '''
    This executes all the functions in an order to explain how select_related and prefetch_related works
    '''
    products_list = list_products()
    # We have all our products, but what’s the problem with this function?
    # Let’s see how many queries this function does into the database:
    