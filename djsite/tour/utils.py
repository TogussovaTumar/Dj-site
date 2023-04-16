from django.core.cache import cache
from django.db.models import Count

from tour.models import *

menu = [{ 'title': "About Site",'url_name': 'about'},
        { 'title': "Add tour",'url_name': 'add_page'},
        { 'title': "Contact Us",'url_name': 'contact'},
]

class DataMixin:
    paginate_by = 3
    def get_user_context(self,**kwargs):
        context = kwargs
        cats = cache.get('cats')
        if not cats:
            cats = Category.objects.annotate(Count('tour'))
            cache.set('cats', cats, 60)

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] =  0
        return context