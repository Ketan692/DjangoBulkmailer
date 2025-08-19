# 🚀 DjangoBulkmailer

DjangoBulkmailer is a Django-based application for sending bulk emails efficiently to multiple recipients. The project provides core features such as user authentication, bulk mail composition, recipient list management, and uses Django's built-in systems for rapid development.

## ✨ Features

- 👤 User authentication and management (login, registration)
- 💌 Compose and send bulk emails to multiple recipients
- 📋 Upload recipient lists via CSV or manual entry
- 📄 Email template support
- 📊 Delivery status tracking (basic)
- 💻 Responsive UI (HTML/CSS, ready for extension)

## 🗂️ Project Structure

```
DjangoBulkmailer/
├── accounts/ # User management (sign up, login, profile)
├── home/ # Bulk mailer logic and app views
├── static/ # Static assets (CSS, JavaScript, images)
├── templates/ # HTML templates for views
├── db.sqlite3 # Default SQLite database
├── manage.py # Django management script
├── requirements.txt # Python dependencies
```

## 🔧 Getting Started

### 🛠️ Prerequisites

- 🐍 Python 3.8 or higher
- 🌐 Django 3.x or 4.x

### ⏳ Installation

1. **Clone the repo:**
    ```
    git clone https://github.com/Ketan692/DjangoBulkmailer.git
    cd DjangoBulkmailer
    ```

2. **Set up a virtual environment:**
    ```
    python -m venv env
    source env/bin/activate      # Linux/macOS
    env\Scripts\activate         # Windows
    ```

3. **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```

4. **Run migrations:**
    ```
    python manage.py migrate
    ```

5. **Start the development server:**
    ```
    python manage.py runserver
    ```

6. **Access the web app:**  
    Visit `http://localhost:8000` in your browser.

## 📫 Email Configuration
Edit `settings.py` to configure your email backend:
```
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = '<your-smtp-host>'
EMAIL_PORT = 587
EMAIL_HOST_USER = '<your-email>'
EMAIL_HOST_PASSWORD = '<your-password>'
EMAIL_USE_TLS = True
```


## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss your ideas.

## 📄 License

MIT License

## 👨‍💻 Author

[Ketan692](https://github.com/Ketan692)

---

 `settings.py` to configure your email backend:
