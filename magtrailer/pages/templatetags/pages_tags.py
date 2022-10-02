from django import template
from pages.models import *

register = template.Library()


@register.simple_tag(name='getcats')
def get_categories():
    return Category.objects.filter(available=True)
