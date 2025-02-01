# Multilingual FAQ Management System

A Django-based project for managing multilingual FAQs with WYSIWYG editor support, REST API integration, Redis caching, and automated translations.

## Features

- *Model Design*: Manage FAQs with multilingual support.
- *WYSIWYG Editor*: Format answers using django-ckeditor.
- *REST API*: Access and manage FAQs via API with language selection.
- *Caching*: Use Redis for efficient data retrieval.
- *Automated Translations*: Leverage Google Translate API for auto-translations.
- *Admin Interface*: User-friendly admin panel for FAQ management.
- *Unit Testing*: Ensure code quality with comprehensive tests.

---

## Installation

### Prerequisites

- Python 3.12
- Redis (via Memurai, WSL, or native installation)
- Virtual Environment (recommended)

### Setup on Windows

1. *Clone the Repository*:
   bash
   git clone <repository-url>
   cd <repository-directory>
   

2. *Create and Activate Virtual Environment*:
   bash
   py -3.12 -m venv venv
   venv\Scripts\activate
   

3. *Install Dependencies*:
   bash
   pip install -r requirements.txt
   

4. *Configure Redis*:
   - *Option 1*: Install [Memurai](https://www.memurai.com/get-memurai).
   - *Option 2*: Use WSL to install Redis:
     bash
     sudo apt update
     sudo apt install redis-server
     sudo service redis-server start
     

5. *Set Up Environment Variables*:
   Create a .env file in the project root:
   ini
   DEBUG=True
   SECRET_KEY=your_secret_key
   REDIS_URL=redis://127.0.0.1:6379/1
   GOOGLE_TRANSLATE_API_KEY=your_google_translate_api_key
   

6. *Apply Migrations*:
   bash
   python manage.py makemigrations
   python manage.py migrate
   

7. *Create Superuser*:
   bash
   python manage.py createsuperuser
   

8. *Run the Server*:
   bash
   python manage.py runserver
   

---

## API Usage

### *Endpoints:*

- *List FAQs*:
  http
  GET /api/faqs/?lang=en
  

- *Retrieve Specific FAQ*:
  http
  GET /api/faqs/<id>/?lang=hi
  

- *Create FAQ*:
  http
  POST /api/faqs/
  Content-Type: application/json

  {
    "question": "What is Django?",
    "answer": "Django is a high-level Python web framework.",
    "language": "en"
  }
  

### *Query Parameters:*

- ?lang=: Specify the language (e.g., en, hi, bn).

---

## Admin Interface

1. Navigate to:
   
   http://127.0.0.1:8000/admin/
   
2. Log in using your superuser credentials.
3. Add, edit, or delete FAQs with multilingual support and rich-text formatting.

---

## Running Tests

Ensure that all functionalities work as expected:

1. *Run Unit Tests*:
   bash
   pytest
   

2. *Lint Code*:
   bash
   flake8
   

---
