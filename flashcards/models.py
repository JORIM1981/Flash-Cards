from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



# Create your models here.
class Deck(models.Model):
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    description = models.TextField(max_length=500, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the canonical URL for a deck."""
        return reverse('flashcards:create_cards', args=[str(self.id)])


class Card(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)

    def __str__(self):
        return self.question


class StudySet(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="student", default='')


class StudentDeck(models.Model):
    studyset = models.ForeignKey(StudySet, on_delete=models.CASCADE, related_name="studyset")
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)


class FlipBox(models.Model):
    frequency = models.SmallIntegerField()

    def __str__(self):
        return str(self.frequency)


class ScoreBoard(models.Model):
    student = models.ForeignKey(StudySet, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    box = models.ForeignKey(FlipBox, on_delete=models.CASCADE)
    updated = models.DateField()
    Flip_date = models.DateField()

    def __str__(self):
        return str(self.card)