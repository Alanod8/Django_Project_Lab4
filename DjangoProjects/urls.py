
from django.contrib import admin
from django.urls import include, path

# Main URL configuration (Tasks 1, 3, and 6)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include("apps.bookmodule.urls")),  # Include bookmodule URLs
    path('users/', include("apps.usermodule.urls")),  # Include usermodule URLs
]
