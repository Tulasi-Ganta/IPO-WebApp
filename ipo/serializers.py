# fields = '__all__'
        # fields = [
        #     'id', 'company_name', 'logo', 'price_band', 'open_date', 'close_date', 
        #     'issue_size', 'issue_type', 'listing_date', 'status',
        #     'ipo_price', 'listing_price', 'listing_gain', 'current_market_price', 
        #     'current_return', 'rhp_pdf', 'drhp_pdf'
        # ]

# from rest_framework import serializers
# from .models import IPO

# class IPOSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = IPO
#         fields = '__all__'


# # serializers.py
# from rest_framework import serializers
# from .models import IPO

# class IPOSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = IPO
#         fields = ['id', 'company_name', 'price_band', 'open_date', 'close_date', 'issue_size', 'issue_type', 'ipo_price', 'listing_price', 'current_market_price', 'status']

from rest_framework import serializers
from .models import IPO

class IPOSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPO
        fields = [
            'id', 'company_name', 'status', 'logo', 'price_band', 'open_date', 'close_date',
            'issue_size', 'issue_type', 'listing_date', 'ipo_price', 'listing_price',
            'listing_gain', 'current_market_price', 'current_return', 'rhp_pdf', 'drhp_pdf'
        ]
