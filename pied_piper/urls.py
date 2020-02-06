from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from app import views as app_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('about/', app_views.about, name='about-view'),
    path('text/', app_views.text_view, name='text-view'),
    path('image/', app_views.image_view, name='image-view'),
    path('image/compress_image/', app_views.image_cmp_view, name='compress_image'),
    path('image/decompress_image/', app_views.image_dcmp_view, name='decompress_image'),
    path('text/compress_text/', app_views.text_cmp_view, name='compress_text'),
    path('text/decompress_text/', app_views.text_dcmp_view, name='decompress_text'),
    path('text/decompress_text/', app_views.text_dcmp_view, name='decompress_text'),
    path('about/piper_piper.html/', app_views.home, name='about-to-home'),
    path('about/piper_piper.html/image/', app_views.image_view, name='about-to-image'),
    path('about/piper_piper.html/text/', app_views.text_view, name='about-to-text'),
    path('about/piper_piper.html/text/compress_text', app_views.text_cmp_view, name='about-to-text_cmp'),
    path('about/piper_piper.html/image/compress_image', app_views.image_cmp_view, name='about-to-image_cmp'),
    path('about/piper_piper.html/text/decompress_text', app_views.image_cmp_view, name='about-to-text_dcmp'),
    path('about/piper_piper.html/image/decompress_image', app_views.image_cmp_view, name='about-to-image_dcmp'),

    path('compressed-file_download/<file_name>/',
         app_views.download_compressed_file_view,
         name='download-compressed-file'),
    path('text-file_download/<file_name>/',
         app_views.download_text_file_view,
         name='download-text-file'),
    path('image-file_download/<file_name>/',
         app_views.download_image_file_view,
         name='download-image-file'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)