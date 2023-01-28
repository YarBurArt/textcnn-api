from django.contrib import admin
from django.urls import path, include

# root url router
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reiapi.urls')),
 ]