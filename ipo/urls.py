from django.urls import path
from .views import (
    IPOListAPIView,
    IPODetailAPIView,
    dashboard,
    export_ipos_csv,
    export_ipos_excel
)

urlpatterns = [
    # Frontend
    path('', dashboard, name='dashboard'),

    # API endpoints
    path('api/ipo/', IPOListAPIView.as_view(), name='ipo_list'),
    path('api/ipo/<int:pk>/', IPODetailAPIView.as_view(), name='ipo_detail'),

    # Export endpoints
    path('api/ipo/export/csv/', export_ipos_csv, name='export_csv'),
    path('api/ipo/export/excel/', export_ipos_excel, name='export_excel'),
]
