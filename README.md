Wooden Bed Booking System

A web-based booking management application developed using **Django** and **Django REST Framework (DRF)**. The system allows customers to book wooden beds online and enables administrators to manage bookings, customers, and bed information efficiently.


Features

* Customer booking and reservation management
* Add, view, update, and delete bookings (CRUD operations)
* Bed management system
* Django Admin Panel for data management
* REST API endpoints using Django REST Framework
* Form validation and database integration
* Responsive and user-friendly interface


Technologies Used

* Python
* Django
* Django REST Framework (DRF)
* SQLite3
* HTML5
* CSS3
* Bootstrap
* JavaScript
* Django Templates
* Django Forms
* Django ORM
* REST APIs
* MVT (Model-View-Template) Architecture


Project Structure

Wooden-Bed-Booking-System/
│
├── RestApp/
├── templates/
├── static/
├── manage.py
├── db.sqlite3
├── requirements.txt
└── README.md

Installation and Setup

1. Clone the repository

bash
git clone https://github.com/yourusername/Wooden-Bed-Booking-System.git
cd Wooden-Bed-Booking-System


2. Create and activate a virtual environment

bash
python -m venv venv


Windows

bash
venv\Scripts\activate


Linux/Mac

bash
source venv/bin/activate


3. Install dependencies

bash
pip install -r requirements.txt


4. Apply migrations

bash
python manage.py migrate


5. Run the development server

bash
python manage.py runserver


Open your browser and visit:

text
http://127.0.0.1:8000/


 API Endpoints

| Method | Endpoint                  | Description          |
| ------ | ------------------------- | -------------------- |
| GET    | `/RestApp/bookings/`      | Get all bookings     |
| POST   | `/RestApp/bookings/`      | Create a new booking |
| PUT    | `/RestApp/bookings/<id>/` | Update a booking     |
| DELETE | `/RestApp/bookings/<id>/` | Delete a booking     |



Screenshots

Add screenshots of:

* Home Page
* Booking Form
* Admin Dashboard
* API Endpoints

Create a folder named `screenshots` and upload the images there.



Live Demo

PythonAnywhere:
https://armishiqbal.pythonanywhere.com/
 

Author

Armish Iqbal
BS Computer Science Student
Islamia University Bahawalpur
GitHub: https://github.com/armishiqbal


