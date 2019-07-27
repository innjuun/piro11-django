from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "QRsystem"

urlpatterns = [
    path('page_a', views.page_a, name="page_a"),
    path('page_b', views.page_b, name="page_b"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)