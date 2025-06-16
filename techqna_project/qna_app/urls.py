# qna_app/urls.py (Updated)
from django.urls import path
from . import views

urlpatterns = [
    # The index view is now handled by the project-level urls.py
    path('', views.index_view, name='index'),  # Main landing page
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # Q&A chat page is now accessed via /app/qna/
    path('qna/', views.qna_chat_view, name='qna_chat'),
    path('api/generate_ai_response/', views.generate_ai_response, name='generate_ai_response'),
]