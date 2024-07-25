from django import template
import women.views as views
from women.models import Category, TagPost

register = template.Library()

@register.inclusion_tag('women/list_categories.html')
def show_categories(cats_selected=0):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cats_selected}


@register.inclusion_tag('women/list_tags.html')
def show_all_tags():
    return {'tags': TagPost.objects.all()}