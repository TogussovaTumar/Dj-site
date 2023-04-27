from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.forms import model_to_dict
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from tour.serializers import TourSerializer

from .forms import *
from .models import *
from .permissions import IsOwnerOrReadOnly
from .utils import DataMixin, menu
from django.contrib.auth.mixins import  LoginRequiredMixin
from rest_framework import generics, viewsets, mixins


def bad_request(request, exception=None):
    return render(request,'tour/errors/error400.html')
def permission_denied(request, exception=None):
    return render(request,'tour/errors/error404.html', {})
def page_not_found(request,exception):
    return render(request, 'tour/errors/error404.html', {})
def server_error(request,exception=None):
    return render(request,'tour/errors/error500.html',{})


class TourHome(DataMixin,ListView):
    model = Tour
    template_name = 'tour/index.html'
    context_object_name = 'tours'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Main Page")
        return  dict(list(context.items())+list(c_def.items()))


    def get_queryset(self):
        return Tour.objects.filter(is_published=True).select_related('cat')


class TourAPIListPagination(PageNumberPagination):
    page_size =3
    page_size_query_param = 'page_size'
    max_page_size = 10000
class TourAPIList(generics.ListCreateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = TourAPIListPagination


class TourAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    # authentication_classes = (TokenAuthentication,)


# class TourViewSet(mixins.CreateModelMixin,
#                   mixins.RetrieveModelMixin,
#                   mixins.UpdateModelMixin,
#                   mixins.DestroyModelMixin,
#                   mixins.ListModelMixin,
#                   GenericViewSet):
#     # queryset = Tour.objects.all()
#     serializer_class = TourSerializer
#
#     def get_queryset
#     (self):
#         pk = self.kwargs.get("pk")
#         if not pk:
#             return Tour.objects.all()[:3]
#
#         return Tour.objects.filter(pk=pk)
#
#     @action(methods=['get'],detail=True)
#     def category(self,request,pk=None):
#         cats = Category.objects.get(pk=pk)
#         return Response({'cats': cats.name})


# class TourAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Tour.objects.all()
#     serializer_class = TourSerializer

# class TourApiView(APIView):
#     def get(self,request):
#         t = Tour.objects.all()
#         return Response({'tours': TourSerializer(t, many=True).data})
#
#     def post(self,request):
#         serializer = TourSerializer(data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'tours': serializer.data})
#
#     def put(self,request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT"})
#
#         try:
#             instance = Tour.objects.get(pk=pk)
#         except:
#             return Response({"error": "Method PUT"})
#
#         serializer = TourSerializer(data = request.data, instance=instance)
#         serializer.is_valid(raise_exception= True)
#         serializer.save()
#         return Response({"tour": serializer.data})
#
#     def delete(self,request,*args,**kwargs):
#         pk = kwargs.get("pk",None)
#         if not pk:
#             return Response({"error": "Method DELETE"})
#
#
#
#         return Response({"tour": "delete tour "+str(pk)})





# class TourApiView(generics.ListAPIView):
#     queryset = Tour.objects.all()
#     serializer_class = TourSerializer


class TourAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes = (IsAdminUser,)

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
    contact_list = Tour.objects.all()
    paginator = Paginator(contact_list,3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'tour/about.html',{'page_obj':page_obj,'menu': menu,'title': 'About Site'})

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


# def login(request):
#     return HttpResponse("Avtorization")

class ContactFormView(DataMixin,FormView):
    form_class = ContactForm
    template_name = 'tour/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Contact")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self,form):
        print(form.cleaned_data)
        return redirect('home')



def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page Not Found</h1>')

def logout_user(request):
    logout(request)
    return redirect('login')

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


class TourCategory(DataMixin,ListView):
    model = Tour
    template_name = 'tour/index.html'
    context_object_name = 'tours'
    allow_empty = False

    def get_queryset(self):
        return Tour.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title='Category - '+ str(c.name),
                                      cat_selected=c.pk)

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


class RegisterUser(DataMixin,CreateView):
    form_class = RegisterUserForm
    template_name = 'tour/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self,*, object_list=None,**kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title ='Registration')
        return dict(list(context.items())+list(c_def.items()))

    def form_valid(self,form):
        user = form.save()
        login(self.request,user)
        return redirect('home')

class LoginUser(DataMixin,LoginView):
    form_class = LoginUserForm
    template_name = 'tour/login.html'

    def get_context_data(self,*, object_list=None,**kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title ='Autorization')
        return dict(list(context.items())+list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')



