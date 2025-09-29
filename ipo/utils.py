from django.http import HttpResponse
import csv
from openpyxl import Workbook
from .models import IPO

# CSV Export
def export_ipos_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="ipos.csv"'

    writer = csv.writer(response)
    writer.writerow(['Company', 'Price Band', 'Open Date', 'Close Date', 'Issue Size', 'Type', 'Status', 'IPO Price', 'Listing Price', 'Current Market Price'])

    for ipo in IPO.objects.all():
        writer.writerow([
            ipo.company_name,
            ipo.price_band,
            ipo.open_date,
            ipo.close_date,
            ipo.issue_size,
            ipo.issue_type,
            ipo.status,
            ipo.ipo_price,
            ipo.listing_price,
            ipo.current_market_price
        ])

    return response

# Excel Export
def export_ipos_excel(request):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="ipos.xlsx"'

    wb = Workbook()
    ws = wb.active
    ws.append(['Company', 'Price Band', 'Open Date', 'Close Date', 'Issue Size', 'Type', 'Status', 'IPO Price', 'Listing Price', 'Current Market Price'])

    for ipo in IPO.objects.all():
        ws.append([
            ipo.company_name,
            ipo.price_band,
            ipo.open_date,
            ipo.close_date,
            ipo.issue_size,
            ipo.issue_type,
            ipo.status,
            ipo.ipo_price,
            ipo.listing_price,
            ipo.current_market_price
        ])

    wb.save(response)
    return response
