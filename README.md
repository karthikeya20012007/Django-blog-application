# Django Blog Application

A full-featured blog application built using **Django**, implementing user authentication, profile management, CRUD operations for posts, pagination, password reset via email, and clean project structure following best practices.

This project was built as a learning and portfolio project to understand real-world Django workflows.

---

## 🚀 Features

- User registration, login, logout
- Password reset via email (secure token-based)
- User profile with profile picture
- Create, read, update, delete (CRUD) blog posts
- Posts filtered by individual users
- Pagination for blog posts
- Authorization (only authors can edit/delete their posts)
- Django Class-Based Views (CBVs)
- Clean Git history (media files excluded)

---

## 🛠️ Tech Stack

- **Backend**: Django
- **Database**: SQLite (development)
- **Authentication**: Django auth system
- **Email**: Gmail SMTP (App Password)
- **Frontend**: Django Templates, Bootstrap
- **Version Control**: Git & GitHub

---

## 📁 Project Structure (simplified)

Django-blog-application/
│
├── blog/ # Blog app (posts, views, urls)
├── users/ # User & profile management
├── django_project/ # Project settings
├── templates/ # HTML templates
├── static/ # Static files (CSS, JS)
├── media/ # ❌ NOT tracked in Git
│ └── profile_pics/ # Profile images
├── manage.py
├── .gitignore
└── README.md


---

## ⚠️ IMPORTANT: Media Folder Setup (Required)

The `media/` folder is **intentionally excluded from Git** to avoid committing user-uploaded files.

### You MUST create this manually after cloning:

```bash
media/
└── profile_pics/
Without this, profile image uploads will not work.

⚙️ Setup Instructions
1️⃣ Clone the repository
git clone https://github.com/karthikeya20012007/Django-blog-application.git
cd Django-blog-application
2️⃣ Create and activate virtual environment
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
3️⃣ Install dependencies
pip install -r requirements.txt
(if requirements.txt is not present, install Django manually)

pip install django python-decouple pillow
4️⃣ Create .env file for email configuration
Create a .env file in the root directory:

EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_gmail_app_password
⚠️ Do NOT commit this file.

5️⃣ Configure email in settings.py
from decouple import config

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
6️⃣ Run migrations
python manage.py migrate
7️⃣ Create superuser (optional)
python manage.py createsuperuser
8️⃣ Create media folders
mkdir media
mkdir media/profile_pics
9️⃣ Run the server
python manage.py runserver
Open:
👉 http://127.0.0.1:8000/

🔐 Password Reset Flow
Users can reset their password using Forgot Password

Secure reset link is sent via email

Gmail SMTP uses App Passwords (2-Step Verification required)

🧠 Key Learning Outcomes
Django Class-Based Views (CBVs)

Authentication & authorization

Secure email handling

Git hygiene (excluding media & secrets)

Real-world Django project structure

📌 Notes
media/ is excluded from version control on purpose

This project is intended for development and learning

In production, media files should be stored using cloud storage (S3, Cloudinary, etc.)

👤 Author
Karthikeya
GitHub: https://github.com/karthikeya20012007

⭐ Acknowledgements
Django Documentation

Corey Schafer’s Django Tutorial Series


---

## ✅ What you should do next

1. Save this as `README.md`
2. Commit it:
```bash
git add README.md
git commit -m "Add project README with setup instructions"
git push