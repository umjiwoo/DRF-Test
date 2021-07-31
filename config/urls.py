from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny


schema_view = get_schema_view(
    openapi.Info(
        title="Booking Open API", # 타이틀
        default_version='v1', # 버전
        description="프로젝트 API 문서", # 설명
    ),
    validators=['flex'],
    public=True,
    permission_classes=(AllowAny,),
)


urlpatterns = [
    path(r'swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(r'swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),
    # django 앱
    path('admin/', admin.site.urls),
    path('v1/', include('booking.urls')),
]
