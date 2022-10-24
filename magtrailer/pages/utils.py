from django.db.models import Count

from .models import *

menu = [{'title': 'ГОЛОВНА', 'url_name': 'home'},
        {'title': 'НАШІ ПРИЧЕПИ', 'url_name': 'all_categories'},
        {'title': 'ДОСТАВКА І ОПЛАТА', 'url_name': 'buy_and_delivery'},
        {'title': 'КОНТАКТИ', 'url_name': 'contacts'},
        {'title': 'ПРО НАС', 'url_name': 'about'}
        ]


class PagesMixin:
    paginate_by = 9

    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        if 'cat_selected' not in context:
            context['cat_selected'] = None
        return context

