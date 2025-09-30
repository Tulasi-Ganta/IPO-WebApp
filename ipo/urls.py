

from django.urls import path
from .views import IPOListAPIView, IPODetailAPIView, export_ipos_csv, export_ipos_excel

urlpatterns = [
    # API endpoints
    path('', IPOListAPIView.as_view(), name='ipo-list'),
    path('<int:pk>/', IPODetailAPIView.as_view(), name='ipo-detail'),

    # Export endpoints
    path('export/csv/', export_ipos_csv, name='export_csv'),
    path('export/excel/', export_ipos_excel, name='export_excel'),
]
