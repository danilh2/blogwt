from blog.models import BlogCategory as Category
from django.template import Library

register = Library()

@register.inclusion_tag('blog/components/categories_list.html', takes_context=True)
def categories_list(context):
    categories = Category.objects.all()
    return {
        'request': context,
        'categories': categories,
        }