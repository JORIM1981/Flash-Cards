from django.contrib import admin
from .models import Deck, Card, StudySet, FlipBox, ScoreBoard, StudentDeck

# Register your models here.
class DeckAdmin(admin.ModelAdmin):
    fields = ['title', 'subject', 'creator', 'description']


class CardAdmin(admin.ModelAdmin):
    fields = ['question', 'answer', 'deck']


class StudySetAdmin(admin.ModelAdmin):
    fields = ['student']

class StudentDeckAdmin(admin.ModelAdmin):
    fields = ['studyset', 'student', 'deck']


class FlipBoxAdmin(admin.ModelAdmin):
    fields = ['frequency']


class ScoreBoardAdmin(admin.ModelAdmin):
    fields = ['student', 'card', 'box', 'updated', 'flip_date']


admin.site.register(Deck, DeckAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(StudySet, StudySetAdmin)
admin.site.register(ScoreBoard, ScoreBoardAdmin)
admin.site.register(FlipBox, FlipBoxAdmin)
admin.site.register(StudentDeck, StudentDeckAdmin)