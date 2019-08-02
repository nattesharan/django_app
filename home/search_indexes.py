from haystack import indexes
from home.models import Post

class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, template_name="search/search_post.txt")
    author = indexes.CharField(model_attr='user')
    pub_date = indexes.DateTimeField(model_attr='created_on')

    def get_model(self):
        return Post
    
    def index_queryset(self, using=None):
        return self.get_model().objects.all()