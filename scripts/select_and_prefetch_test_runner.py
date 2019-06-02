from extra_topics.utils import (list_products, list_products_with_select_related, 
                                list_categories, list_categories_with_prefetch_related,
                                categories_list_active_subcategories,
                                categories_list_active_subcategories_using_prefetch_attr,
                                categories_list_active_subcategories_without_prefetch_attr)
from extra_topics.decorators import query_info

def run():
    '''
    This executes all the functions in an order to explain how select_related and prefetch_related works
    '''
    # 1) Select related isslustration
    products_list = list_products()
    # We have all our products, but what’s the problem with this function?
    # Let’s see how many queries this function does into the database:
    '''
    I created one debugger decorator to see how many queries each util function takes, 
    it shows the number of the queries and the time in seconds for each example
    select_related is used for feoreign keys or one to many fields or one to one relation ships
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
    print("#######################################################")
    # Congrats! Now we did only 1 query instead of 501, it’s a real improvement

    # 2) Prefetch related illustration
    # prefetch related is used for many to many relationships
    categories_list = list_categories()

    query_info(list_categories)()
    print("#######################################################")
    '''
    The above funtion took 51 queries to fetch the data
    '''
    categories_fetched_with_prefetch_related = list_categories_with_prefetch_related()

    assert categories_fetched_with_prefetch_related == categories_list

    query_info(list_categories_with_prefetch_related)()
    '''
    why we have two queries?
    the prefetch_related made the JOIN using Python rather than in the database.
    In this case, Django made two queries and then join the results into one queryset for us.
    '''
    print("#######################################################")

    '''
    Let’s create a new function that will return only the active subcategories using the prefetch_related
    '''

    query_info(categories_list_active_subcategories)()
    print("#######################################################")
    '''
    WOW! We increased the number of queries, how it’s possible?????
    Calm down, there is a reason for this:
    When we use the prefetch related we are saying to Django we want all the results to be JOINED, but when we use the 
    filter(is_active=True) we are changing the primary query and then Django doesn’t JOIN the right result
    That’s why we have 52 queries, 51 queries iterating over the categories and 1 query to get all the results in prefetch.s for us.
    '''
    # Let’s see how to solve this problem using the new Prefetch introduced recently by Django
    # 1) Using Prefetch with to_attr
    query_info(categories_list_active_subcategories_using_prefetch_attr)()
    print("#######################################################")
    # Great!! Now again we have only two queries
    
    # Let’s how we could achieve the same result without using the to_attr parameter.
    query_info(categories_list_active_subcategories_without_prefetch_attr)()
    print("#######################################################")