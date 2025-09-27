# LostFound_App
Project: Online Lost & Found Management System (Django)

Project Overview

A web application to streamline campus lost & found operations. Students can report lost/found items (with images), search items, submit claims with proof, and track claim status. Admins verify found items and approve ownership transfers.

Objective

Provide a secure, searchable, and role-based platform where students and admins manage lost & found items efficiently.

Key Features

User authentication (students) and admin role

Report lost or found items with images

Search and filter items (by category, date, location, status)

Claim items with proof of ownership upload

Admin verification workflow for claims and ownership transfer

User dashboard to track reported items and claim statuses

Suggested Tech Stack

Python 3.10+

Django 4.x

HTML / CSS / JavaScript

Bootstrap or Tailwind CSS

SQLite (development) / PostgreSQL (production)

Module Distribution (Suggested)

Member 1: Item Reporting, File Uploads & User Dashboard

Member 2: Search, Claim System & Admin Verification

Django Concepts Covered

Models, Views, Templates, ORM queries & filters, Forms/ModelForms, File uploads, Authentication, Role-based access, CRUD operations

Quick Start (Development)

1.Clone the repo

git clone <your-repo-url>
cd campus-lost-and-found

2.Create and activate a virtual environment

python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

3.Install requirements

pip install -r requirements.txt

4.Apply migrations

python manage.py migrate

5.Create superuser (pre-created credentials below) or create one manually

# To create manually (optional)
python manage.py createsuperuser

6.Collect static files (for production)

python manage.py collectstatic

7.Run the development server

python manage.py runserver

Open http://127.0.0.1:8000/ in your browser.

Superuser (Development/Test Account)

Username: spidey
Password: spidey@1234

Important: These credentials are included for convenience during development/testing only. Change the password before deploying to production.
