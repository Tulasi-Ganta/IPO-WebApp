



# from django.shortcuts import render
# from django.http import HttpResponse
# from rest_framework import generics, filters
# from rest_framework.filters import OrderingFilter
# from rest_framework.permissions import IsAuthenticated
# from django_filters.rest_framework import DjangoFilterBackend
# from .models import IPO
# from .serializers import IPOSerializer
# from .pagination import IPOPagination
# import csv
# from openpyxl import Workbook

# # -------------------- FRONTEND PAGE --------------------
# def dashboard(request):
#     """Renders the main IPO Dashboard HTML."""
#     return render(request, 'index.html')


# # -------------------- API VIEWS --------------------
# class IPOListAPIView(generics.ListAPIView):
#     queryset = IPO.objects.all()
#     serializer_class = IPOSerializer
#     pagination_class = IPOPagination
#     permission_classes = [IsAuthenticated]  # 🔒 JWT Auth

#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, OrderingFilter]
#     filterset_fields = ['status']  # filter by status
#     search_fields = ['company_name']  # search by company name
#     ordering_fields = ['open_date', 'ipo_price', 'listing_price', 'current_market_price']
#     ordering = ['open_date']  # default ordering


# class IPODetailAPIView(generics.RetrieveAPIView):
#     queryset = IPO.objects.all()
#     serializer_class = IPOSerializer
#     lookup_field = 'pk'
#     permission_classes = [IsAuthenticated]  # 🔒 JWT Auth


# # -------------------- EXPORT CSV --------------------
# def export_ipos_csv(request):
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="ipos.csv"'

#     writer = csv.writer(response)
#     writer.writerow([
#         'Company Name', 'Status', 'Price Band', 'Open Date', 'Close Date',
#         'Issue Size', 'Issue Type', 'IPO Price', 'Listing Price', 'Current Market Price'
#     ])

#     for ipo in IPO.objects.all():
#         writer.writerow([
#             ipo.company_name, ipo.status, ipo.price_band, ipo.open_date, ipo.close_date,
#             ipo.issue_size, ipo.issue_type, ipo.ipo_price, ipo.listing_price, ipo.current_market_price
#         ])
#     return response


# # -------------------- EXPORT EXCEL --------------------
# def export_ipos_excel(request):
#     response = HttpResponse(
#         content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
#     )
#     response['Content-Disposition'] = 'attachment; filename="ipos.xlsx"'

#     wb = Workbook()
#     ws = wb.active
#     ws.title = "IPO Data"

#     ws.append([
#         'Company Name', 'Status', 'Price Band', 'Open Date', 'Close Date',
#         'Issue Size', 'Issue Type', 'IPO Price', 'Listing Price', 'Current Market Price'
#     ])

#     for ipo in IPO.objects.all():
#         ws.append([
#             ipo.company_name, ipo.status, ipo.price_band, ipo.open_date, ipo.close_date,
#             ipo.issue_size, ipo.issue_type, ipo.ipo_price, ipo.listing_price, ipo.current_market_price
#         ])

#     wb.save(response)
#     return response

















from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, filters
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from .models import IPO
from .serializers import IPOSerializer
from .pagination import IPOPagination
import csv
from openpyxl import Workbook

# -------------------- FRONTEND PAGE --------------------
def dashboard(request):
    """Renders the main IPO Dashboard HTML."""
    return render(request, 'index.html')


# -------------------- API VIEWS --------------------
class IPOListAPIView(generics.ListAPIView):
    """
    API endpoint for listing all IPOs with pagination,
    filtering, search, and ordering.
    Protected by JWT.
    """
    queryset = IPO.objects.all()
    serializer_class = IPOSerializer
    pagination_class = IPOPagination
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, OrderingFilter]
    filterset_fields = ['status']  # filter by status
    search_fields = ['company_name']  # search by company name
    ordering_fields = ['open_date', 'ipo_price', 'listing_price', 'current_market_price']
    ordering = ['open_date']  # default ordering


class IPODetailAPIView(generics.RetrieveAPIView):
    """API endpoint to fetch a single IPO by its ID (JWT protected)."""
    queryset = IPO.objects.all()
    serializer_class = IPOSerializer
    lookup_field = 'pk'
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


# -------------------- EXPORT CSV --------------------
def export_ipos_csv(request):
    """Exports all IPOs to a CSV file (JWT protected if needed)."""
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="ipos.csv"'

    writer = csv.writer(response)
    writer.writerow([
        'Company Name', 'Status', 'Price Band', 'Open Date', 'Close Date',
        'Issue Size', 'Issue Type', 'IPO Price', 'Listing Price', 'Current Market Price'
    ])

    for ipo in IPO.objects.all():
        writer.writerow([
            ipo.company_name, ipo.status, ipo.price_band, ipo.open_date, ipo.close_date,
            ipo.issue_size, ipo.issue_type, ipo.ipo_price, ipo.listing_price, ipo.current_market_price
        ])
    return response


# -------------------- EXPORT EXCEL --------------------
def export_ipos_excel(request):
    """Exports all IPOs to an Excel (.xlsx) file (JWT protected if needed)."""
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename="ipos.xlsx"'

    wb = Workbook()
    ws = wb.active
    ws.title = "IPO Data"

    ws.append([
        'Company Name', 'Status', 'Price Band', 'Open Date', 'Close Date',
        'Issue Size', 'Issue Type', 'IPO Price', 'Listing Price', 'Current Market Price'
    ])

    for ipo in IPO.objects.all():
        ws.append([
            ipo.company_name, ipo.status, ipo.price_band, ipo.open_date, ipo.close_date,
            ipo.issue_size, ipo.issue_type, ipo.ipo_price, ipo.listing_price, ipo.current_market_price
        ])

    wb.save(response)
    return response
