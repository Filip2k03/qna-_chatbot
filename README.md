TechQ&A Bot: AI-Powered Question & Answer Platform for Tech Students
🚀 Project Overview
The TechQ&A Bot is an interactive web application designed for technology students to test and expand their knowledge using an AI-powered question-and-answer system. Built with Django for the backend, Tailwind CSS for a sleek UI, and Alpine.js for dynamic frontend interactions, this platform allows users to engage in Q&A sessions with the Google Gemini AI, earn scores, and compete on a global leaderboard.

This project is ideal for competitive events or personal learning, offering a modern and responsive user experience with both light and dark modes.

✨ Features
User Authentication: Secure registration and login system powered by Django's built-in authentication.

AI-Powered Q&A: Engage in conversational Q&A sessions with the Google Gemini (Flash) AI model.

Real-time Scoring: Earn points for each question answered by the AI, with your current score updated instantly.

Global Leaderboard: View and track top scores from all users on a dynamic leaderboard.

Responsive Design: Optimized for seamless experience across various devices (desktop, tablet, mobile) using Tailwind CSS.

Light & Dark Mode: User-friendly theme toggle with preference persistence.

Interactive UI/UX: Enhanced user experience with smooth transitions, animations, and Alpine.js-driven components (e.g., password visibility toggle, dynamic messages).

Simple Setup: Uses CDN links for frontend libraries (Tailwind CSS, Alpine.js, Font Awesome) for quick development setup without a Node.js build pipeline.

🛠️ Technologies Used
Backend:

Python 3.x

Django 5.x: Web framework for backend logic, routing, and database management.

python-dotenv: For managing environment variables (like API keys).

google-generativeai: Python client library for interacting with Google Gemini API.

SQLite3 (Development): Default database for Django.

Frontend:

HTML5

Tailwind CSS (CDN): Utility-first CSS framework for rapid UI development and styling.

Alpine.js (CDN): A minimalist JavaScript framework for adding declarative and reactive behavior to HTML.

Font Awesome (CDN): For scalable vector icons.

Custom CSS: For specific animations and chat bubble styling.

AI Model:

Google Gemini (Flash)

🚀 Getting Started
Follow these instructions to set up and run the project locally.

Prerequisites
Python 3.8+

pip (Python package installer)

A Google Gemini API Key. You can get one from the Google AI Studio.

Installation
Clone the repository (or create the project structure manually):

git clone https://github.com/your-username/techqna_project.git # Replace with your repo URL
cd techqna_project

Create and activate a Python virtual environment:

python -m venv venv
# On Linux/macOS:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

Install Python dependencies:

pip install -r requirements.txt

(Ensure you have a requirements.txt file at your project root containing the dependencies from previous steps.)

Set up Environment Variables:
Create a .env file in the root of your techqna_project directory and add your Gemini API Key:

# .env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY_HERE
# You can also add a Django secret key for production environments (optional for development)
# DJANGO_SECRET_KEY='your_super_secret_key_here'

Remember to replace YOUR_GEMINI_API_KEY_HERE with your actual key.

Apply Database Migrations:

python manage.py makemigrations qna_app
python manage.py migrate

Create a Django Superuser (for Admin Panel access):

python manage.py createsuperuser

Follow the prompts to create an administrator user.

Running the Application
Start the Django development server:

python manage.py runserver

Access the application:
Open your web browser and navigate to:

http://127.0.0.1:8000/

You will land on the index.html welcome page. From there, you can register a new account or log in.

📂 Project Structure
techqna_project/
├── .env                  # Environment variables
├── manage.py             # Django's command-line utility
├── db.sqlite3            # Default SQLite database
├── venv/                 # Python virtual environment
├── qna_app/              # Django application for Q&A features
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py         # Defines Score model
│   ├── tests.py
│   ├── urls.py           # App-specific URL patterns (e.g., /app/login, /app/qna)
│   └── views.py          # Logic for Q&A, authentication, API calls
├── templates/            # Django HTML templates
│   ├── base.html         # Base template with global styles, CDNs, theme logic
│   ├── index.html        # Landing page
│   ├── login.html        # User login form
│   ├── register.html     # User registration form
│   └── qna_chat.html     # Main Q&A chat interface
└── techqna_project/      # Django project core
    ├── __init__.py
    ├── asgi.py
    ├── settings.py       # Main Django settings (API key, installed apps, etc.)
    ├── urls.py           # Project-level URL patterns (e.g., /admin, /)
    └── wsgi.py

📄 License
This project is open-source and available under the MIT License.
