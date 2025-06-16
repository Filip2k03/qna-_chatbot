# 💡 TechQ&A Bot: AI-Powered Q&A Platform for Tech Students

🚀 **TechQ&A Bot** is an interactive web platform built for technology students to test and expand their knowledge through an AI-driven Q&A system. It features real-time scoring, a global leaderboard, and a sleek, responsive design with both light and dark modes.

Built with **Django** (backend), **Tailwind CSS**, and **Alpine.js** (frontend), this project leverages the power of **Google Gemini AI (Flash)** to simulate conversational learning and competition.

---

## ✨ Features

- 🔐 **User Authentication** — Secure registration and login with Django's built-in auth system.
- 🤖 **AI-Powered Q&A** — Engage in real-time Q&A with the Google Gemini Flash model.
- 🏅 **Scoring System** — Earn points per question, updated instantly.
- 🌍 **Global Leaderboard** — Track top user scores dynamically.
- 📱 **Responsive UI** — Works perfectly on desktop, tablet, and mobile.
- 🌗 **Light/Dark Mode** — Theme toggle with saved preferences.
- ⚡ **Interactive UX** — Smooth transitions and reactivity with Alpine.js.
- 🧩 **Quick Setup** — Frontend via CDN (no Node.js setup required).

---

## 🛠️ Tech Stack

### 🔧 Backend
- Python 3.x  
- Django 5.x  
- SQLite3 (for development)  
- `python-dotenv` – For managing `.env`  
- `google-generativeai` – Google Gemini API integration  

### 🎨 Frontend
- HTML5  
- Tailwind CSS (via CDN)  
- Alpine.js (via CDN)  
- Font Awesome (via CDN)  
- Custom CSS (chat UI, theme transitions)

### 🤖 AI Model
- [Google Gemini (Flash)](https://aistudio.google.com/)

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.8+
- pip (Python package installer)
- A valid [Google Gemini API Key](https://aistudio.google.com/app/apikey)

---

### 📥 Installation

```bash
# Clone the repository
git clone https://github.com/your-username/techqna_project.git
cd techqna_project

# Create and activate virtual environment
python -m venv venv
# For macOS/Linux:
source venv/bin/activate
# For Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
