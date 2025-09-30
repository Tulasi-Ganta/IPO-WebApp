
# from django.shortcuts import render
# from django.http import HttpResponse
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import IPO
# from .serializers import IPOSerializer
# import csv
# from openpyxl import Workbook
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import generics

# # Dashboard page
# def dashboard(request):
#     return render(request, 'index.html')

# # API Views
# class IPOListAPIView(APIView):
#     def get(self, request):
#         ipos = IPO.objects.all()
#         serializer = IPOSerializer(ipos, many=True)
#         return Response({"count": len(serializer.data), "results": serializer.data})

# class IPODetailAPIView(APIView):
#     def get(self, request, pk):
#         try:
#             ipo = IPO.objects.get(pk=pk)
#             serializer = IPOSerializer(ipo)
#             return Response(serializer.data)
#         except IPO.DoesNotExist:
#             return Response({"error": "IPO not found"}, status=404)

# # Export CSV
# def export_ipos_csv(request):
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="ipos.csv"'
#     writer = csv.writer(response)
#     writer.writerow(['Company Name', 'Status', 'Price Band', 'Open Date', 'Close Date', 'Issue Size', 'Issue Type', 'IPO Price', 'Listing Price', 'Current Market Price'])
#     for ipo in IPO.objects.all():
#         writer.writerow([ipo.company_name, ipo.status, ipo.price_band, ipo.open_date, ipo.close_date, ipo.issue_size, ipo.issue_type, ipo.ipo_price, ipo.listing_price, ipo.current_market_price])
#     return response

# # Export Excel
# def export_ipos_excel(request):
#     response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
#     response['Content-Disposition'] = 'attachment; filename="ipos.xlsx"'
#     wb = Workbook()
#     ws = wb.active
#     ws.append(['Company Name', 'Status', 'Price Band', 'Open Date', 'Close Date', 'Issue Size', 'Issue Type', 'IPO Price', 'Listing Price', 'Current Market Price'])
#     for ipo in IPO.objects.all():
#         ws.append([ipo.company_name, ipo.status, ipo.price_band, ipo.open_date, ipo.close_date, ipo.issue_size, ipo.issue_type, ipo.ipo_price, ipo.listing_price, ipo.current_market_price])
#     wb.save(response)
#     return response


from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics,filters
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import IPO
from .serializers import IPOSerializer
import csv
from openpyxl import Workbook
from .pagination import IPOPagination  # create this file as mentioned

# Dashboard page
def dashboard(request):
    return render(request, 'index.html')

# API Views
# class IPOListAPIView(generics.ListAPIView):
#     queryset = IPO.objects.all()
#     serializer_class = IPOSerializer
#     filter_backends = [DjangoFilterBackend, OrderingFilter]
#     filterset_fields = ['status', 'company_name']  # filter by status or company name
#     ordering_fields = ['open_date', 'ipo_price', 'listing_price', 'current_market_price']
#     ordering = ['open_date']  # default ordering
#     pagination_class = IPOPagination

class IPOListAPIView(generics.ListAPIView):
    queryset = IPO.objects.all()
    serializer_class = IPOSerializer
    pagination_class = IPOPagination

    # Filters
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, OrderingFilter]
    filterset_fields = ['status']                 
    search_fields = ['company_name']             
    ordering_fields = ['open_date', 'ipo_price', 'listing_price', 'current_market_price']
    ordering = ['open_date']           

class IPODetailAPIView(generics.RetrieveAPIView):
    queryset = IPO.objects.all()
    serializer_class = IPOSerializer
    lookup_field = 'pk'

# Export CSV
def export_ipos_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="ipos.csv"'
    writer = csv.writer(response)
    writer.writerow(['Company Name', 'Status', 'Price Band', 'Open Date', 'Close Date', 'Issue Size', 'Issue Type', 'IPO Price', 'Listing Price', 'Current Market Price'])
    for ipo in IPO.objects.all():
        writer.writerow([ipo.company_name, ipo.status, ipo.price_band, ipo.open_date, ipo.close_date, ipo.issue_size, ipo.issue_type, ipo.ipo_price, ipo.listing_price, ipo.current_market_price])
    return response

# Export Excel
def export_ipos_excel(request):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="ipos.xlsx"'
    wb = Workbook()
    ws = wb.active
    ws.append(['Company Name', 'Status', 'Price Band', 'Open Date', 'Close Date', 'Issue Size', 'Issue Type', 'IPO Price', 'Listing Price', 'Current Market Price'])
    for ipo in IPO.objects.all():
        ws.append([ipo.company_name, ipo.status, ipo.price_band, ipo.open_date, ipo.close_date, ipo.issue_size, ipo.issue_type, ipo.ipo_price, ipo.listing_price, ipo.current_market_price])
    wb.save(response)
    return response
