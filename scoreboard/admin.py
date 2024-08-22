
# Register your models here.
from django.contrib import admin
from .models import SpeakingScoreboard, ListeningScoreboard, ListeningUserRanking, SpeakingUserRanking


class ListeningUserRankingInline(admin.StackedInline):
    model = ListeningUserRanking
    extra = 1
    ordering = ('score', )

class SpeakingUserRankingInline(admin.StackedInline):
    model = SpeakingUserRanking
    extra = 1
    ordering = ('score', )

@admin.register(SpeakingScoreboard)
class SpeakingScoreboardAdmin(admin.ModelAdmin):
    inlines = [SpeakingUserRankingInline]

    list_display = ('exercise_title', 'exercise_number_of_plays')
    search_fields = ('exercise__title',)
    
    def exercise_title(self, obj):
        return obj.exercise.title
    exercise_title.admin_order_field = 'exercise__title'
    exercise_title.short_description = 'Exercise Title'
    
    def exercise_number_of_plays(self, obj):
        return obj.exercise.number_of_plays
    exercise_number_of_plays.admin_order_field = 'exercise__number_of_plays'
    exercise_number_of_plays.short_description = 'Number of Plays'

@admin.register(ListeningScoreboard)
class ListeningScoreboardAdmin(admin.ModelAdmin):
    inlines = [ListeningUserRankingInline]
    list_display = ('exercise_title', 'exercise_number_of_plays')
    search_fields = ('exercise__title',)
    
    def exercise_title(self, obj):
        return obj.exercise.title
    exercise_title.admin_order_field = 'exercise__title'
    exercise_title.short_description = 'Exercise Title'
    
    def exercise_number_of_plays(self, obj):
        return obj.exercise.number_of_plays
    exercise_number_of_plays.admin_order_field = 'exercise__number_of_plays'
    exercise_number_of_plays.short_description = 'Number of Plays'
