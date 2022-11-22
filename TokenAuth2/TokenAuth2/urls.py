from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from api.auth import CustomAuthToken
# creating Router Object
router = DefaultRouter()
#Register StudentViewSet with Router
router.register('studentapi',views.StudentReadOnlyModelViewSet,basename = 'student')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
    path('gettoken/',CustomAuthToken.as_view())
]
