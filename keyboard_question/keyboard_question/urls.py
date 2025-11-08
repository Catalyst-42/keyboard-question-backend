"""
URL configuration for keyboard_question project.

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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from keyboard_api import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from keyboard_api.views import HealthCheckView

schema_view = get_schema_view(
    openapi.Info(
        title="Keyboard Metrics API",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'corpus', views.CorpusViewSet)
router.register(r'keyboards', views.KeyboardViewSet)
router.register(r'layouts', views.LayoutViewSet)
router.register(r'metrics', views.MetricViewSet)
router.register(r'frequencies', views.FrequencyViewSet)
router.register(r'bigramms', views.BigrammViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include(router.urls)),
    path('api/health/', HealthCheckView.as_view(), name='health-check'),  

    path('swagger<format>/', schema_view.without_ui(), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger'), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc'), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
)
