from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_uno.urls')),
    path('blogs/', include('app_uno.urls')),
    path('blogs/new/', include('app_uno.urls')),
    path('blogs/created/', include('app_uno.urls')),
    path('blogs/<int:number>/', include('app_uno.urls')),
    path('blogs/<int:number>/edit/', include('app_uno.urls')),
    path('blogs/<int:number>/delete/', include('app_uno.urls')),
]
