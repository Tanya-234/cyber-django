"""
URL configuration for securepass project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include,re_path
from authentication.views import HomeView, switch_language
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.views import serve
from django.conf.urls.i18n import i18n_patterns



urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('authentication/',include('authentication.urls')),
    path('', HomeView.as_view(), name='home'),
    path('incidents/',include('incidents.urls')),
    path('switch_language/<str:language_code>/', switch_language, name='switch_language'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# path('switch-language/', views.switch_language, name='switch_language'),
