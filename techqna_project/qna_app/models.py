from django.db import models
from django.contrib.auth.models import User # Django's built-in User model

class Score(models.Model):
    """
    Model to store user scores for the Q&A game.
    Each user has one score entry, which is updated.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='qna_score')
    score = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Score: {self.score}"

    class Meta:
        # Order scores by highest first for the leaderboard
        ordering = ['-score']
