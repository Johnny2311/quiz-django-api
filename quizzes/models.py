from django.db import models
from django.conf import settings


class Quiz(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    times_taken = models.IntegerField(default=0, editable=False)

    @property
    def question_count(self):
        return self.questions.count()

    class Meta:
        verbose_name_plural = "Quizzes"
        ordering = ['id']

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(
        Quiz,
        related_name='questions',  # if not setted, use question_set instead
        on_delete=models.CASCADE
    )
    prompt = models.CharField(max_length=255)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.prompt


class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        related_name='answers',
        on_delete=models.CASCADE
    )
    text = models.CharField(max_length=255)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
