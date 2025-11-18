
from django.urls import path
from viewer.views import upload_file, view_file
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', upload_file, name='upload'),
    path('view/<str:filename>/', view_file, name='view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
