# myproject/urls.py

from django.contrib import admin
from django.urls import path, include # Importez 'include' ici

urlpatterns = [
    path('admin/', admin.site.urls),
    # Ajoutez un chemin pour inclure les URL patterns de votre application "core"
    path('', include('core.urls')),
]
   