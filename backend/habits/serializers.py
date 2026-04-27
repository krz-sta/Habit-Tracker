from rest_framework import serializers
from .models import Habit, HabitLog

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ['id', 'owner', 'title', 'desc', 'start_date', 'type']
        read_only_fields = ['id', 'owner']
    

class HabitLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitLog
        fields = ['id', 'habit', 'log_date']