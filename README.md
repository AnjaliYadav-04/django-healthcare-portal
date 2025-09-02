# 🏥 Django Healthcare Portal

A web-based healthcare portal built with **Django**, featuring custom user authentication, patient & doctor dashboards, and modern UI with animations.  

This project was created as part of a task/assignment to demonstrate Django development, authentication, and frontend integration with Bootstrap & Lottie animations.

---

## 🚀 Features

- 🔑 **Custom User Authentication**
  - Signup with **Doctor** / **Patient** role
  - Profile picture upload & preview
  - Secure login & logout system  

- 🧑‍⚕️ **Role-based Dashboards**
  - Doctor Dashboard
  - Patient Dashboard

- 🎨 **Modern UI**
  - Bootstrap 5 + Animate.css
  - Floating background animations
  - Lottie animations on forms
  - Glassmorphism-style cards & buttons

- 📋 **Forms**
  - Signup with profile picture preview
  - Animated inputs with validation errors
  - Responsive two-column layout

---

## 🛠️ Tech Stack

- **Backend:** Django 5
- **Frontend:** Bootstrap 5, Animate.css, Lottie Animations
- **Database:** SQLite (default, can be switched to PostgreSQL/MySQL)
- **Authentication:** Django’s built-in auth + custom `CustomUser` model

---
## 📂 Project Structure
Django_Task/
│── accounts/ # Custom user app
│ ├── migrations/
│ ├── templates/
│ │ ├── signup.html
│ │ ├── login.html
│ │ ├── doctor_dashboard.html
│ │ ├── patient_dashboard.html
│ ├── forms.py
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│
│── Django_Task/ # Main project settings
│ ├── settings.py
│ ├── urls.py
│
│── templates/
│ ├── base.html # Global layout
│
│── manage.py


---

## ⚡ Setup Instructions

1. **Clone the repository**
 
- git clone https://github.com/AnjaliYadav-04/django-healthcare-portal.git
- cd django-healthcare-portal
2. **Create virtual environment**
python -m venv venv
- source venv/bin/activate   # Mac/Linux
- venv\Scripts\activate      # Windows

3. **Install dependencies**
- Django==5.0.2
- django-widget-tweaks==1.5.0
- asgiref==3.7.2
- sqlparse==0.4.4
- tzdata==2023.4


4. **Apply migrations**
- python manage.py makemigrations
- python manage.py migrate

5. **Create superuser**
- python manage.py createsuperuser
- Run development server
- python manage.py runserver


6. **Open in browser:**
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/admin
- http://127.0.0.1:8000/login
- http://127.0.0.1:8000/signup

---

## 🙌 Author
**👤 Anjali Yadav**
- GitHub: https://github.com/AnjaliYadav-04
- LinkedIn: https://www.linkedin.com/in/anjali-yadav-464099257

---

## ⭐ Acknowledgements
- Django
- Bootstrap 5
- Animate.css
- LottieFiles

---


