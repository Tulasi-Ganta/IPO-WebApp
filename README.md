# Bluestock Fintech IPO Web App & REST API

## 📌 Project Overview
This project is a Django-based web application for managing IPO (Initial Public Offering) data.  
It provides:
- REST API (Django REST Framework)
- CSV & Excel export
- Frontend IPO Dashboard (HTML, CSS, JS)
- Filtering, sorting, searching, and pagination
- Media handling for logos and PDFs

---

## 🚀 Features
- IPO Dashboard with filters (status, company, date, returns)
- REST API (`/api/ipo/`, `/api/ipo/<id>/`)
- Export IPO data (CSV & Excel)
- Django Admin panel for managing IPOs
- Countdown for upcoming/ongoing IPOs
- Dummy data population using `python manage.py seed_ipo`

---

## ⚙️ Tech Stack
- **Backend**: Python 3.12.3, Django 5.0.6, Django REST Framework
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (default, can switch to PostgreSQL/MySQL)
- **Exports**: CSV, Excel
- **Media**: Static & Media files support

---

## 🔑 Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/proipo.git
   cd proipo
