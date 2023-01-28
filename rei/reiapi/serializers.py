from rest_framework import serializers

from .models import Question


# reform data from database to byte for tcp/udp protocol
class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'request_char', 'answer_char', 'request_date')
