# Django Healthcare Portal with Blog System
A comprehensive web-based healthcare portal built with Django, featuring custom user authentication, patient & doctor dashboards, blog system, and modern UI with animations.
This project was created as part of a task/assignment to demonstrate Django development, authentication, content management, and frontend integration with Bootstrap & Lottie animations.

---

## 🚀 Features
### 🔑 Custom User Authentication
- Signup with Doctor / Patient role selection
- Profile picture upload & preview
- Secure login & logout system
- Address information collection

### 🧑‍⚕️ Role-based Dashboards
- Doctor Dashboard: Access to blog creation and management
- Patient Dashboard: Health blog browsing and reading

### 📝 Integrated Blog System
**1. Doctor Features:**
- Create, edit, and manage blog posts
- Categorize posts (Mental Health, Heart Disease, Covid19, Immunization)
- Save posts as drafts or publish immediately
- View personal blog statistics

**2. Patient Features:**
- Browse published blog posts by category
- Read full articles with proper formatting
- Search and filter functionality

 ### 🎨 Modern UI
- Bootstrap 5 + Animate.css
- Floating background animations
- Lottie animations on forms
- Glassmorphism-style cards & buttons
- Responsive design for all devices

### 📋 Forms
- Signup with profile picture preview
- Blog creation with image upload
- Animated inputs with validation errors
- Responsive multi-column layouts

### 🛠️ Tech Stack
- **Backend:** Django 5
- **Frontend:** Bootstrap 5, Animate.css, Lottie Animations
- **Database:** SQLite (default, can be switched to PostgreSQL/MySQL)
- **Authentication:** Django's built-in auth + custom CustomUser model
- **File Storage:** Local media storage (can be configured for AWS S3)

---

## 📂 Project Structure
**Django_Task/**
│
├── accounts/                 # Custom user app
│   ├── migrations/
│   ├── templates/
│   │   ├── registration/    # Auth templates
│   │   │   ├── login.html
│   │   │   ├── logout.html
│   │   ├── signup.html
│   │   ├── doctor_dashboard.html
│   │   ├── patient_dashboard.html
│   │   ├── create_blog.html
│   │   ├── my_blogs.html
│   │   ├── blog_list.html
│   │   ├── blog_detail.html
│   ├── forms.py             # Signup & Blog forms
│   ├── models.py            # CustomUser, Category, BlogPost
│   ├── views.py             # Authentication & Blog views
│   ├── admin.py             # Custom admin configuration
│   └── urls.py
│
**├── Django_Task/**            # Main project settings
│   ├── settings.py
│   ├── urls.py
│
**├── templates/**
│   ├── base.html           # Global layout
│
**├── media/**                  # Uploaded files (auto-created)
│   ├── profiles/
│   └── blog_images/
│
└── manage.py

---

## ⚡ Setup Instructions
**1. Clone the repository**
- git clone https://github.com/AnjaliYadav-04/django-healthcare-portal.git
- cd django-healthcare-portal
  
**2. Create virtual environment**
- python -m venv venv
- source venv/bin/activate  # Mac/Linux
- venv\Scripts\activate     # Windows
  
**3. Install dependencies**
- pip install Django==5.0.2 django-widget-tweaks==1.5.0

**4. Apply migrations**
- python manage.py makemigrations
- python manage.py migrate

**5. Create superuser**
- python manage.py createsuperuser

**6. Create initial categories (Run in Django shell)**
- python manage.py shell
python
from accounts.models import Category
categories = ['Mental Health', 'Heart Disease', 'Covid19', 'Immunization']
for cat in categories:
    Category.objects.get_or_create(name=cat, slug=cat.lower().replace(' ', '-'))
  
**7. Run development server**
- python manage.py runserver

---
 
## Access the application:

- **Main site:** http://127.0.0.1:8000/
- **Admin panel:** http://127.0.0.1:8000/admin
- **Login:** http://127.0.0.1:8000/login
- **Signup:** http://127.0.0.1:8000/signup
- **Blog list**: http://127.0.0.1:8000/blog/list/

---

## 🎯 User Roles & Capabilities
**👨‍⚕️ Doctors Can:**
- Create and publish blog posts
- Save posts as drafts for later editing
- View their own blog posts
- Manage post categories
- Use rich text formatting for content

**👤 Patients Can:**
- Browse published blog posts
- Filter posts by categories
- Read full articles with proper formatting
- View doctor information and credentials

---

## 📝 Blog System Features
**1. 4 Default Categories:** Mental Health, Heart Disease, Covid19, Immunization
**2. Rich Content Support:** Text formatting, images, and summaries
**3. Draft System:** Save unfinished posts for later completion
**4. Author Attribution:** Each post shows the doctor author
**5. Content Truncation:** Automatic summary shortening for list views
**6. Category Filtering:** Browse posts by specific health topics

---

## 🔧 Customization
**Adding New Categories:**
- Access Django Admin at /admin
- Navigate to Accounts → Categories
- Add new health categories as needed

**Modifying Blog Features:**
- Edit models.py to add new fields like:
- Featured posts
- Reading time estimates

**Comment systems**
- Like/dislike functionality

Database Configuration:
To switch to MySQL/PostgreSQL, update settings.py:

---

## 🙌 Author
**👤 Anjali Yadav**

- **GitHub:** https://github.com/AnjaliYadav-04
- **LinkedIn:** https://www.linkedin.com/in/anjali-yadav-464099257

---

### ⭐ Acknowledgements
- Django Framework
- Bootstrap 5
- Animate.css
- Lottie Animations

Medical content references from reputable health organizations

