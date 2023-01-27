from django.shortcuts import render

from rest_framework import viewsets

from .serializers import QuestionSerializer
from .models import Question


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by('request_char')
    serializer_class = QuestionSerializer
