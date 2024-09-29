from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cafeteria.views import coffe_view,new_coffe_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", coffe_view, name='inicio_list'),
    path("new_coffe", new_coffe_view, name='novo_cafe_list'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
