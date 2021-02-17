from rest_framework import serializers

from .models import Quiz, Question, Answer


class QuizSerializer(serializers.ModelSerializer):

    def get_fullname(self, obj):
        return obj.author.first_name + ' ' + obj.author.last_name

    def get_question_count(self, obj):
        return obj.question_count

    author_fullname = serializers.SerializerMethodField("get_fullname")
    question_count = serializers.SerializerMethodField("get_question_count")

    class Meta:
        model = Quiz
        fields = [
            'id',
            'title',
            'author_fullname',
            'question_count',
            'created_at',
        ]


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = [
            'id',
            'text',
            'correct',
            'question',
        ]


class QuestionSerializer(serializers.ModelSerializer):

    answers = AnswerSerializer(
        read_only=True,
        many=True
    )

    class Meta:
        model = Question
        fields = [
            'id',
            'quiz',
            'prompt',
            'answers'
        ]
