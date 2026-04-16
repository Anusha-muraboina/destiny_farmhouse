"""
URL configuration for destiny_farm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
# from resort.sitemaps import clean_sitemap
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
# from resort.sitemaps import StaticSitemap, RoomCategorySitemap
from resort.sitemaps import StaticViewSitemap, BlogSitemap, RoomSitemap
from django.conf.urls.static import static

from django.shortcuts import render
def custom_404(request, exception):
    return render(request, "resort/404.html", status=404)

sitemaps = {
    "static": StaticViewSitemap,
    "blogs": BlogSitemap,
    "rooms": RoomSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('destiny_admin/', include('destiny_admin.urls')),
    path('', include('resort.urls')),
    path('blog/', include('blog.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    
    # path("test404/", test_404),

    path(
        "robots.txt",
        TemplateView.as_view(
            template_name="robots.txt",
            content_type="text/plain"
        ),
    ),
    
]
handler404 = "destiny_farm.urls.custom_404"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


