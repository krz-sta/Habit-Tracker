from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import HabitSerializer, HabitLogSerializer
from .models import Habit, HabitLog
from rest_framework import status
from rest_framework.response import Response


# Create your views here.
class HabitView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = HabitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response({'message': 'Habit created.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def get(self, request):
        habits = Habit.objects.filter(owner=request.user)
        serializer = HabitSerializer(habits, many=True)
        return Response(serializer.data)
        
    
    def put(self, request, pk):
        try:
            habit = Habit.objects.get(pk=pk, owner=request.user)
        except Habit.DoesNotExist:
            return Response({'message': 'Habit not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = HabitSerializer(habit, data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response({'message': 'Habit updated.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pk):
        try:
            habit = Habit.objects.get(pk=pk, owner=request.user)
        except Habit.DoesNotExist:
            return Response({'message': 'Habit not found.'}, status=status.HTTP_404_NOT_FOUND)
        habit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class HabitLogView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, pk):
        try:
            habit = Habit.objects.get(pk=pk, owner=request.user)
        except Habit.DoesNotExist:
            return Response({'message': 'Habit not found.'},status=status.HTTP_404_NOT_FOUND)
        
        if habit.type == 'bad':
            return Response({'message': "You can't log a bad habit."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = HabitLogSerializer(data={'habit': habit.id, 'log_date': request.data.get('log_date')})
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Habit logged.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
    def delete(self, request, pk, log_pk):
        try:
            habit_log = HabitLog.objects.get(pk=log_pk, habit__owner=request.user)
        except HabitLog.DoesNotExist:
            return Response({'message': 'Habit log not found.'}, status=status.HTTP_404_NOT_FOUND)
        habit_log.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class AllHabitLogsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        habit_logs = HabitLog.objects.filter(habit__owner=request.user)
        serializer = HabitLogSerializer(habit_logs, many=True)
        return Response(serializer.data)