"""chelgradirni URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

from core.views import CoolerListView

import core

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='core/index.html')),
    url(r'^structure/$', TemplateView.as_view(template_name='core/structure.html')),
    url(r'^catalog/$', CoolerListView.as_view(), name='cooler-list'),
    url(r'^photos/$', TemplateView.as_view(template_name='core/photos.html')),
    url(r'^contacts/$', TemplateView.as_view(template_name='core/contacts.html')),
]

from django.conf import settings
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)