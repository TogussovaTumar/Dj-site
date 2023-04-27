from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import  path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenRefreshView

# import settings
from tour.views import *
from rest_framework import routers



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tour.urls')),
    path('captcha/', include('captcha.urls')),
    path('api/v1/tour/', TourAPIList.as_view()),
    path('api/v1/tour/<int:pk>/', TourAPIUpdate.as_view()),
    path('api/v1/tourdelete/<int:pk>/', TourAPIDestroy.as_view()),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]

if settings.DEBUG:
    import  debug_toolbar

    urlpatterns=[
        path('__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

handler404 = pageNotFound