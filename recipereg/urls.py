from django.contrib import admin
from django.urls import path, include  # Remove the second import of path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app1.urls')),
]
