from django import template
from animals.models import Category,Curator

register=template.Library()

@register.simple_tag()
def show_categ():
    caty=Category.objects.all()
    return caty

@register.simple_tag()
def show_curator():
    caty=Curator.objects.all()
    return caty



