from django.db.models import Count

from tour.models import *

menu = [{ 'title': "About Site",'url_name': 'about'},
        { 'title': "Add tour",'url_name': 'add_page'},
        { 'title': "Login",'url_name': 'login'},
]

class DataMixin:
    def get_user_context(self,**kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('tour'))

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] =  0
        return context