from django.db import models

# Create your models here.

# used for demonstrating select_related and prefetch_related
class Category(models.Model):
    name = models.CharField(max_length=120)
    is_active = models.BooleanField(default=True)
    # Recursive relationships using an intermediary model are always defined as non-symmetrical – that is, 
    # with symmetrical=False
    sub_categories = models.ManyToManyField('self', symmetrical=False)

    def __str__(self):
        return self.name

# used for demonstrating select_related and prefetch_related
class Product(models.Model):
    title = models.CharField(max_length=120)
    category = models.ForeignKey(Category, related_name='products')

    def __str__(self):
        return self.title
