from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import HabitSerializer, HabitLogSerializer
from .models import Habit
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
    
    
    def get_object(self, pk, user):
        try:
            return Habit.objects.get(pk=pk, owner=user)
        except Habit.DoesNotExist:
            return None
        
    
    def put(self, request, pk):
        habit = self.get_object(pk, request.user)
        if not habit:
            return Response({'message': 'Habit not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = HabitSerializer(habit, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Habit updated.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pk):
        habit = self.get_object(pk, request.user)
        if not habit:
            return Response({'message': 'Habit not found.'}, status=status.HTTP_404_NOT_FOUND)
        habit.delete()
        return Response({'message': 'Habit deleted.'}, status=status.HTTP_200_OK)