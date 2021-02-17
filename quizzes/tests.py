from django.test import TestCase
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User

from .models import Quiz, Question, Answer


class SimpleTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='test',
            email='test@test.com'
        )
        self.quiz = Quiz.objects.create(
            author=self.user,
            title='test'
        )
        self.question = Question.objects.create(
            quiz=self.quiz,
            prompt='test'
        )

    def test_quiz_viewset(self):
        # list
        response = self.client.get(reverse('quiz-list'))
        self.assertEqual(response.status_code, 200)

        # create
        data = {
            'author': self.user.id,
            'title': 'test'
        }
        self.client.force_login(user=self.user)
        response = self.client.post(reverse('quiz-list'), data, content_type='application/json')
        self.assertEqual(response.status_code, 201)

        # update
        data['title'] = 'updated_test'
        response = self.client.put(reverse('quiz-detail', kwargs={'pk': 1}), data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        # delete
        response = self.client.delete(reverse('quiz-detail', kwargs={'pk': 2}), data, content_type='application/json')
        self.assertEqual(response.status_code, 204)

        # questions
        response = self.client.get(reverse('quiz-questions', kwargs={'pk': 1}), content_type='application/json')
        self.assertEqual(response.status_code, 200)

        # all questions
        response = self.client.get(reverse('quiz-all-questions', kwargs={'pk': 1}), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_question_viewset(self):
        # list
        response = self.client.get(reverse('question-list'))
        self.assertEqual(response.status_code, 200)

        # create
        data = {
            'quiz': self.quiz.id,
            'prompt': 'test'
        }
        response = self.client.post(reverse('question-list'), data, content_type='application/json')
        self.assertEqual(response.status_code, 201)

        # update
        data['prompt'] = 'updated_test'
        response = self.client.put(reverse('question-detail', kwargs={'pk': 1}), data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        # delete
        response = self.client.delete(reverse('question-detail', kwargs={'pk': 2}), data, content_type='application/json')
        self.assertEqual(response.status_code, 204)

    def test_answer_viewset(self):
        # list
        response = self.client.get(reverse('answer-list'))
        self.assertEqual(response.status_code, 200)

        # create
        data = {
            'question': self.question.id,
            'text': 'test',
            'correct': False
        }
        response = self.client.post(reverse('answer-list'), data, content_type='application/json')
        self.assertEqual(response.status_code, 201)

        # update
        data['prompt'] = 'updated_test'
        response = self.client.put(reverse('answer-detail', kwargs={'pk': 1}), data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        # delete
        response = self.client.delete(reverse('answer-detail', kwargs={'pk': 1}), data, content_type='application/json')
        self.assertEqual(response.status_code, 204)
