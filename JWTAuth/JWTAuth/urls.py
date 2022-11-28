from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

# creating Router Object
router = DefaultRouter()
#Register StudentViewSet with Router
router.register('studentapi',views.StudentRModelViewSet,basename = 'student')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('gettoken/',TokenObtainPairView.as_view(),name="token_obtained_pair"),
    path('refreshtoken/',TokenRefreshView.as_view(),name="token_refresh"),
    path('verifytoken/',TokenVerifyView.as_view(),name="token_verify"),
]