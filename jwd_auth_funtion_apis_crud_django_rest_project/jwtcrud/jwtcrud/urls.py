from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import token_obtain_pair,token_refresh

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include('app1.urls')),
    path('v1/',include('authapp.urls')),
    path('v1/access/',token_obtain_pair),
    path('v1/refresh/',token_refresh),
]
