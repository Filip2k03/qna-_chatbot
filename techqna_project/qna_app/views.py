import os
import google.generativeai as genai
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.conf import settings
import json # For handling JSON payload from frontend
from .models import Score
from django.contrib.auth.models import User

# Configure Google Gemini API
# The API key is loaded from .env via Django settings
genai.configure(api_key=settings.GEMINI_API_KEY)

# Initialize the Gemini model
# 'gemini-pro' is generally good for text. Use 'gemini-pro-vision' for multi-modal.
# Or use 'gemini-2.0-flash' as requested by previous context
model = genai.GenerativeModel('gemini-2.0-flash')

def index_view(request):
    """
    Renders the main landing page (index.html).
    """
    return render(request, 'index.html')

def register_view(request):
    """
    Handles user registration.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create a score entry for the new user
            Score.objects.create(user=user, score=0)
            login(request, user) # Log the user in after registration
            return redirect('qna_chat')
        else:
            # Add form errors to messages
            for field, errors in form.errors.items():
                for error in errors:
                    # You might want to use Django's messages framework here
                    # from django.contrib import messages
                    # messages.error(request, f"{field}: {error}")
                    print(f"Error in {field}: {error}")
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    """
    Handles user login.
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('qna_chat')
        else:
            # Add form errors to messages
            for field, errors in form.errors.items():
                for error in errors:
                    print(f"Error in {field}: {error}")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required # Ensure user is logged in to access this view
def logout_view(request):
    """
    Logs out the current user.
    """
    logout(request)
    return redirect('login') # Redirect to login page after logout

@login_required
def qna_chat_view(request):
    """
    Renders the main Q&A chat interface.
    Also fetches the current user's score and the global leaderboard.
    """
    # Get or create the user's score
    user_score, created = Score.objects.get_or_create(user=request.user)

    # Get the global leaderboard
    # Using .values() to get dictionary-like objects, simpler for templates/JSON
    # .values() does not include the password hash, only username and score
    leaderboard = Score.objects.select_related('user').all().order_by('-score')[:10] # Top 10
    leaderboard_data = []
    for entry in leaderboard:
        leaderboard_data.append({
            'username': entry.user.username,
            'score': entry.score,
            'last_updated': entry.last_updated.strftime('%Y-%m-%d') # Format date for display
        })

    context = {
        'current_score': user_score.score,
        'leaderboard': leaderboard_data,
        'current_username': request.user.username,
    }
    return render(request, 'qna_chat.html', context)

@login_required
@require_POST # Only allow POST requests for this view
def generate_ai_response(request):
    """
    Handles the AI question-answering logic.
    Receives user question, calls Gemini API, returns AI response.
    Also updates the user's score.
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_question = data.get('question')
            chat_history = data.get('chat_history', []) # Expect chat history from frontend

            if not user_question:
                return JsonResponse({'error': 'No question provided.'}, status=400)

            # Convert frontend chat history format to Gemini API format
            # This ensures the conversation context is maintained for the AI
            gemini_chat_history = []
            for entry in chat_history:
                gemini_chat_history.append({'role': entry['role'], 'parts': [{'text': entry['text']}]})

            # Start a chat session with the model
            chat = model.start_chat(history=gemini_chat_history)
            response = chat.send_message(user_question)

            ai_response_text = response.text

            # Update user's score (e.g., 10 points per successful Q&A)
            user_score_obj, created = Score.objects.get_or_create(user=request.user)
            user_score_obj.score += 10
            user_score_obj.save()

            return JsonResponse({
                'ai_response': ai_response_text,
                'new_score': user_score_obj.score
            })

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method.'}, status=405) # Should not be reached due to @require_POST

