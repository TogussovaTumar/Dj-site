from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView, CreateView
from .forms import *
from .models import *
from .utils import DataMixin,menu
from django.contrib.auth.mixins import  LoginRequiredMixin



def user_context(title):
    pass


class TourHome(DataMixin,ListView):
    model = Tour
    template_name = 'tour/index.html'
    context_object_name = 'tours'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Main Page")
        return  dict(list(context.items())+list(c_def.items()))


    def get_queryset(self):
        return Tour.objects.filter(is_published=True)

# def index(request):
#     tours = Tour.objects.all()
#     context ={
#         'tours': tours,
#         'menu': menu,
#         'title': 'Main Page',
#         'cat_selected': 0,
#     }
#     return render(request,'tour/index.html',context=context)

def about(request):
    return render(request,'tour/about.html',{'menu': menu,'title': 'About Site'})

class AddPage(LoginRequiredMixin,CreateView,DataMixin):
    form_class = AddTourForm
    template_name = 'tour/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="ADD Tour")
        return dict(list(context.items())+list(c_def.items()))




# def addpage(request):
#     if request.method == 'POST':
#         form = AddTourForm(request.POST, request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data)
#                 form.save()
#                 return redirect('home')
#     else:
#         form = AddTourForm()
#     return render(request, 'tour/addpage.html', {'menu': menu, 'form': form, 'title': 'Add page'})


def login(request):
    return HttpResponse("Avtorization")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page Not Found</h1>')


class ShowTour(DetailView,DataMixin):
    model = Tour
    template_name = 'tour/tour.html'
    slug_url_kwarg = 'tour_slug'
    context_object_name = 'tour'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['tour'])
        return dict(list(context.items())+list(c_def.items()))


# def show_tour(request, tour_slug):
#     tour = get_object_or_404(Tour, slug=tour_slug)
#
#     context = {
#         'tour': tour,
#         'menu': menu,
#         'name': tour.name,
#         'cat_selected':tour.cat_id,
#
#     }
#     return render(request, 'tour/tour.html', context=context)


class TourCategory(ListView,DataMixin):
    model = Tour
    template_name = 'tour/index.html'
    context_object_name = 'tours'
    allow_empty = False

    def get_queryset(self):
        return Tour.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Category - '+ str(context['tours'][0].cat),
                                      cat_selected=context['tours'][0].cat_id)

        return dict(list(context.items())+list(c_def.items()))

# def show_category(request, cat_id):
#     tours = Tour.objects.filter(cat_id=cat_id)
#
#     if len(tours) == 0:
#         raise Http404()
#
#     context = {
#         'tours': tours,
#         'menu': menu,
#         'title': 'Regions',
#         'cat_selected': cat_id,
#     }
#     return render(request, 'tour/index.html', context=context)

