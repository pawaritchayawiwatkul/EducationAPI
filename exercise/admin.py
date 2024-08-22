from django.contrib import admin
from .models import ListeningPractice, ListeningQuestion, SpeakingTargets, SpeakingPractice
from category.models import ListeningPracticeCategory
from django.forms import BaseInlineFormSet

class ListeningInline(admin.StackedInline):
    model = ListeningQuestion
    extra = 1

class ListeningCategoryInline(admin.TabularInline):
    model = ListeningPracticeCategory.practices.through
    extra = 1

@admin.register(ListeningPractice)
class ListeningPractice(admin.ModelAdmin):
    inlines = [ListeningInline, ListeningCategoryInline]

    list_display = ('title', 'code', 'number_of_plays')
    search_fields = ('title', 'code')
    fields = ('title', 'image_url')
    # filter_vertical = ('category', )

class SpeakingInline(admin.StackedInline):
    model = SpeakingTargets
    extra = 1

@admin.register(SpeakingPractice)
class SpeakingPractice(admin.ModelAdmin):
    inlines = [SpeakingInline]

    list_display = ('title', 'practice_type',  'code', 'number_of_plays')
    search_fields = ('title', 'code')
    fields = ('title', 'image_url', 'practice_type')
    # filter_horizontal = ('practice_type', )