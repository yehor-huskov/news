from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('', include('getpackage.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('docs/', include_docs_urls(title='My API title'))
]
