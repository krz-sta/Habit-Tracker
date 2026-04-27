from django.db import models
from django.contrib.auth.models import User

class Habit(models.Model):
    class Type(models.TextChoices):
        GOOD = 'good'
        BAD = 'bad'
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    start_date = models.DateField()
    type = models.CharField(max_length=10, choices=Type.choices)
    
    def __str__(self):
        return self.title


class HabitLog(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    log_date = models.DateField()
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['habit', 'log_date'], name='unique_log_for_habit')
        ]