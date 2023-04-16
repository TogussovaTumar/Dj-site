from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import  path, include

# import settings
from tour.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tour.urls')),
    path('captcha/', include('captcha.urls')),

]
if settings.DEBUG:
    import  debug_toolbar

    urlpatterns=[
        path('__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

handler404 = pageNotFound