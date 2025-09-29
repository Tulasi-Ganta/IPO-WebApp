# from django.contrib import admin
# from .models import IPO


# admin.site.register(IPO)


# # Register the IPO model
# @admin.register(IPO)
# class IPOAdmin(admin.ModelAdmin):
#     list_display = ('company_name', 'status', 'open_date', 'close_date', 'ipo_price', 'listing_price')
#     list_filter = ('status', 'open_date', 'close_date')
#     search_fields = ('company_name',)



from django.contrib import admin
from .models import IPO

@admin.register(IPO)
class IPOAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'status', 'open_date', 'close_date', 'ipo_price', 'listing_price')
    list_filter = ('status',)
    search_fields = ('company_name',)
