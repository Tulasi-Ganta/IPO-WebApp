
# from django.contrib import admin
# from django.urls import path, include
# from ipo import views

# urlpatterns = [
#     path('admin/', admin.site.urls),

#     # Include ipo.urls directly (no extra prefix)
#     path('', include('ipo.urls')),

#     # Home/dashboard page
#     path('', views.dashboard, name='home'),
# ]



from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ipo.urls')),

    # JWT Token endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # login
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # refresh token
]
