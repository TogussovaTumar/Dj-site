from django.urls import path, include, re_path
from.views import *


urlpatterns = [
    path('', TourHome.as_view(),name='home'),
    path('about/',about,name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('login/', login, name='login'),
    path('tour/<slug:tour_slug>/', ShowTour.as_view(),name='tour'),
    path('category/<slug:cat_slug>/', TourCategory.as_view(), name='category'),

]

