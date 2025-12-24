# Needly 

Needly is a service booking web application built with Django.  
It allows users to discover services, view details, book appointments, and manage bookings through a clean and user-friendly interface.

---

##  Features

- User authentication (Signup, Login, Logout)
- Browse services by category
- Service detail pages
- Booking system with date & time selection
- User booking management (My Bookings)
- Booking status management (Pending, Confirmed, Completed, Cancelled)
- Admin booking status control
- Search functionality
- Clean UI using Tailwind CSS

---

##  Tech Stack

- **Backend**: Django
- **Frontend**: HTML, Tailwind CSS
- **Database**: SQLite (development)
- **Authentication**: Django Auth
- **Version Control**: Git & GitHub

---

## ️ Installation & Setup

```bash
git clone https://github.com/subeyyr/needly.git
cd needly
python -m venv venv
source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

