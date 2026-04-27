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
        items = Habit.objects.filter(owner=request.user)
        serializer = HabitSerializer(items, many=True)
        return Response(serializer.data)
    