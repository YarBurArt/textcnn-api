from rest_framework import serializers

from .models import Question


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('request_char', 'answer_char', 'response_date')
