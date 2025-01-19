from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render  # Import the render function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # Include the accounts app URLs
    path('', lambda request: render(request, 'accounts/home.html'), name='home'),# Use the render function correctly
]
