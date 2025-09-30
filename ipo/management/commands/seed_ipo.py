from django.core.management.base import BaseCommand
from ipo.models import IPO
from datetime import date, timedelta
import random

class Command(BaseCommand):
    help = 'Seed the database with dummy IPO data'

    def handle(self, *args, **kwargs):
        IPO.objects.all().delete()  # clear existing data

        statuses = ['upcoming', 'ongoing', 'listed']
        companies = ['Alpha Corp', 'Beta Ltd', 'Gamma Inc', 'Delta PLC', 'Epsilon LLC']

        for i in range(10):
            status = random.choice(statuses)
            open_date = date.today() + timedelta(days=random.randint(-10, 10))
            close_date = open_date + timedelta(days=5)
            ipo_price = round(random.uniform(100, 500), 2)
            listing_price = round(ipo_price + random.uniform(-50, 100), 2)
            current_market_price = round(listing_price + random.uniform(-20, 50), 2)

            IPO.objects.create(
                company_name=random.choice(companies) + f" {i+1}",
                price_band=f"{ipo_price}-{ipo_price+10}",
                open_date=open_date,
                close_date=close_date,
                issue_size=f"{random.randint(10, 100)} Cr",
                issue_type=random.choice(['Book Built', 'Fixed Price']),
                listing_date=open_date + timedelta(days=10) if status == 'listed' else None,
                status=status,
                ipo_price=ipo_price,
                listing_price=listing_price if status != 'upcoming' else None,
                current_market_price=current_market_price if status == 'listed' else None
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded IPO data!'))
