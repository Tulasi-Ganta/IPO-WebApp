# from django.urls import path
# from .views import IPOListAPIView, IPODetailAPIView
# from .views import upcoming_ipos

# urlpatterns = [
#     path('', upcoming_ipos, name='home'),
#     path('ipo/', IPOListAPIView.as_view(), name='ipo-list'),
#     path('ipo/<int:pk>/', IPODetailAPIView.as_view(), name='ipo-detail'),
# ]



# from .views import IPOListAPIView, IPODetailAPIView, upcoming_ipos, ipo_counts

# urlpatterns = [
#     path('', upcoming_ipos, name='home'),
#     path('ipo/', IPOListAPIView.as_view(), name='ipo-list'),
#     path('ipo/<int:pk>/', IPODetailAPIView.as_view(), name='ipo-detail'),
#     path('ipo-counts/', ipo_counts, name='ipo-counts'),  # <-- new URL
# ]

# from django.views.generic import TemplateView

# urlpatterns = [
#     path('', TemplateView.as_view(template_name="index.html"), name='home'),
#     path('ipo/', IPOListAPIView.as_view(), name='ipo-list'),
#     path('ipo/<int:pk>/', IPODetailAPIView.as_view(), name='ipo-detail'),
#     path('ipo-counts/', ipo_counts, name='ipo-counts'),
# ]


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
