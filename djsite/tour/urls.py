from django.urls import path, include, re_path
from django.views.decorators.cache import cache_page

from.views import *


urlpatterns = [
    path('',TourHome.as_view(),name='home'),
    path('about/',about,name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    path('tour/<slug:tour_slug>/', ShowTour.as_view(),name='tour'),
    path('category/<slug:cat_slug>/', TourCategory.as_view(), name='category'),

]



