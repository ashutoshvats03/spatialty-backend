from django.contrib import admin
from django.urls import path
from myapp import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/register/', views.RegisterView.as_view(), name='register'),
    path('api/login/', views.LoginView.as_view(), name='login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/dashboard/', views.Dashboard.as_view(), name='Dashboard'),
    path('api/adminLogin/', views.AdminLogin.as_view(), name='AdminLogin'),
    path('api/deleteUser/<int:userid>/', views.DeleteUser.as_view(), name='DeleteUser'),
    path('api/addUser/', views.AddUser.as_view(), name='AddUser'),
    path('api/modifyUser/', views.ModifyUser.as_view(), name='ModifyUser'),
    path('api/healthy/', views.Healthy.as_view(), name='Healthy'),
    path('api/profile/', views.ProfileView.as_view(), name='Profile'),
    path('api/calculation/', views.CalculationView.as_view(), name='Calculation'),
]
if settings.DEBUG:
    urlpatterns += static('/api' + settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

