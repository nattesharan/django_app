from functools import wraps
import time
from django.db import connection, reset_queries

def query_info(func):
    """Basic decorator to which gives the query info."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("func: ", func.__name__)
        reset_queries()
        start = time.time()
        start_queries = len(connection.queries)
        result = func(*args, **kwargs)
        end = time.time()
        end_queries = len(connection.queries)
        print("queries:", end_queries - start_queries)
        print("took: %.2fs" % (end - start))
        return result
    return wrapper
