from extra_topics.utils import list_products, list_products_with_select_related
from extra_topics.decorators import query_info

def run():
    '''
    This executes all the functions in an order to explain how select_related and prefetch_related works
    '''
    products_list = list_products()
    # We have all our products, but what’s the problem with this function?
    # Let’s see how many queries this function does into the database:
    '''
    I created one debugger decorator to see how many queries each util function takes, 
    it shows the number of the queries and the time in seconds for each example
    '''
    query_info(list_products)()
    print("#######################################################")

    '''
    Wow! 501 queries for that simple piece of code?? What happened?

    For each time we access one foreign key that is not in cache, another
    query will be made to retrieve the value.

    In our case, we accessing the category inside a loop, one query will be made for each time the loop executes.
    
    To avoid this high number of queries when accessing foreign keys or one to one fields we can use the select_related 
    method.
    '''
    products_fetched_with_select_related = list_products_with_select_related()

    assert products_fetched_with_select_related == products_list

    query_info(list_products_with_select_related)()

    # Congrats! Now we did only 1 query instead of 501, it’s a real improvement

