💹 Bluestock Fintech IPO Web App & REST API
📌 Project Overview

This project is a Django-based web application for managing IPO (Initial Public Offering) data.
It provides:

REST API (Django REST Framework)

CSV & Excel export

Frontend IPO Dashboard (HTML, CSS, JS)

Filtering, sorting, searching, and pagination

Media handling for logos and PDFs

🚀 Features

✅ Display a list of IPOs with details:

Company Name, Price Band, Open/Close Dates, Issue Size, Issue Type

IPO Price, Listing Price, Current Market Price

✅ Status Badges: Upcoming, Ongoing, Listed, Closed
✅ Search by company name
✅ Filter by IPO status
✅ Sort by Open Date, Listing Gain, Current Return
✅ Pagination (5 items per page)
✅ Export IPO data as CSV or Excel
✅ Dark Mode toggle
✅ API protected with JWT authentication
✅ Responsive design

⚙️ Tech Stack

Backend: Python 3.12.3, Django 5.0.6, Django REST Framework

Frontend: HTML, CSS, JavaScript, Bootstrap 5

Database: SQLite (default, can switch to PostgreSQL/MySQL)

APIs: JWT Authentication for secure data access

Exports: CSV, Excel

Media: Static & Media files support

Others: openpyxl (Excel export), Pillow (image handling)

## 🔑 Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Tulasi-GantaIPO-WebApp.git
   cd IPO-WebApp


2.Create Virtual Environment & Install Dependencies: 
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows

#Install dependencies
pip install -r requirements.txt


3.Database Setup:
# Update PostgreSQL credentials in settings.py
python manage.py migrate
python manage.py createsuperuser  # create admin account


4.Run Server
python manage.py runserver

5.Access Dashboard
Open in browser: http://127.0.0.1:8000/



🔑 JWT Authentication (API)

1.Obtain Token
POST /api/token/
Content-Type: application/json

{
  "username": "Admin1",
  "password": "Admin@912"
}


2.Response
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc2MDYxNjIzNywiaWF0IjoxNzYwNTI5ODM3LCJqdGkiOiJhMGIzODg5MjllMDU0ZDM3OWMxMDczMjg0MGVkYjQxMCIsInVzZXJfaWQiOiIyIn0.yVSdNwYV5Lvfsj4-E0o_Q0FdzZE-JCZIkiBC3eg7vRA",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzYwNTMwMTM3LCJpYXQiOjE3NjA1Mjk4MzcsImp0aSI6ImVmYWQ5NDhkMjc0YzQyYjFhYmMwMGIwMmFhMTg5MmE1IiwidXNlcl9pZCI6IjIifQ.-4q-FYqykQjw5LnIYcnxKogGU7YcmR6Yw-Fe_l5KFMA"
}


3.Use Access Token for Protected APIs

GET /api/ipo/
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzYwNTMwMTM3LCJpYXQiOjE3NjA1Mjk4MzcsImp0aSI6ImVmYWQ5NDhkMjc0YzQyYjFhYmMwMGIwMmFhMTg5MmE1IiwidXNlcl9pZCI6IjIifQ.-4q-FYqykQjw5LnIYcnxKogGU7YcmR6Yw-Fe_l5KFMA



## Screenshots :

### Dashboard
![Dashboard](screenshots/ipo_dashbord.jpg)
![status](screenshots/ipo_status.jpg)
![filter](screenshots/ipo_filter.jpg)
![search](screenshots/ipo_search.jpg)
![csv](screenshots/ipo_csv.jpg)
![excel](screenshots/ipo_excel.jpg)



## File Structure
proipo/
├── docs/                  # Documentation folder
├── ipo/                   # Main Django app
│   ├── migrations/        # Django migrations
│   ├── templates/         # HTML templates
│   │   └── index.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   ├── pagination.py
│   └── tests.py
├── ipo_project/           # Django project folder
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── logos/                 # Logos for IPO companies
├── media/                 # Uploaded media files (PDFs, etc.)
├── screenshots/           # Screenshots for README or docs
├── static/                # CSS, JS, images
├── templates/             # Additional templates
├── venv/                  # Python virtual environment
├── .gitignore             # Git ignore file
├── db.sqlite3             # SQLite database file
├── manage.py              # Django management script
├── README.md              # Project documentation
└── requirements.txt       # Python dependencies


📌 References

Django Documentation

Django REST Framework

Bootstrap 5
