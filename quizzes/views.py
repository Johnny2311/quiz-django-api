from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Quiz, Question, Answer
from .serializers import QuizSerializer, QuestionSerializer, AnswerSerializer
from .paginations import OneByOnePagination


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    @property
    def paginator(self):
        if self.action == 'questions':
            if not hasattr(self, '_paginator'):
                self._paginator = OneByOnePagination()
            return self._paginator
        return None

    @action(detail=True, methods=['get'])
    def questions(self, request, pk=None):
        questions = Question.objects.filter(quiz_id=pk)

        page = self.paginate_queryset(questions)
        if page is not None:
            serializer = QuestionSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = QuestionSerializer(
            questions,
            many=True
        )
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def all_questions(self, request, pk=None):
        questions = Question.objects.all()
        serializer = QuestionSerializer(
            questions,
            many=True
        )
        return Response(serializer.data)


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
