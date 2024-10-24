# Property Rental Management Platform

Description
The Property Rental Management Platform is a comprehensive Django-based web application that connects property owners and tenants. It provides a user-friendly interface for property owners to list their rental properties and for tenants to search, apply for, and manage rental agreements.

Features
- Separate authentication for Admins, Property Owners, and Tenants
- Property listing management (CRUD operations)
- Rental application system
- Booking and rental agreement management
- Payment tracking
- Review and feedback system for properties and landlords
- Responsive design with a custom background

Tech Stack

- Backend: Django
- Frontend: HTML, CSS (Bootstrap), JavaScript
- Database: SQLite (default Django database)

Installation
1. Create a virtual environment and activate it:
   python -m venv venv
   venv\Scripts\activate
   
2. Install the required packages:
   pip install django

3. Apply migrations:
   python manage.py makemigrations
   python manage.py migrate
   
4. Create a superuser:
   python manage.py createsuperuser
   
5. Run the development server:
   python manage.py runserver

6. Open your browser and navigate to `http://127.0.0.1:8000`

 Usage
1. Admin:
   - Access the admin panel at '/admin'
   - Manage users, properties, and reported issues

2. Property Owner:
   - Register as a property owner
   - List properties, update availability, and communicate with tenants

3. Tenant:
   - Register as a tenant
   - Browse properties, apply for rentals, and manage rental agreements

Project Structure
property_rental_platform/
│
├── accounts/
├── properties/
├── rentals/
├── reviews/
├── static/
├── templates/
├── manage.py
├── requirements.txt
└── README.md
