from rest_framework import viewsets

from .serializers import QuestionSerializer
from .models import Question


# to link serialization data with routers
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by('request_char')
    serializer_class = QuestionSerializer
