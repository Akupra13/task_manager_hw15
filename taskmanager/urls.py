# taskmanager/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.views import APIView
from rest_framework.response import Response
# корень
class RootView(APIView):
    def get(self, request):
        return Response({"message": "Welcome to the Task Manager API!"})
urlpatterns = [
    # Маршруты для JWT 
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Маршруты для админа
    path('admin/', admin.site.urls),
   
    path('api/', include('tasks.urls')),
    # корень
    path('', RootView.as_view(), name='root'),
]
