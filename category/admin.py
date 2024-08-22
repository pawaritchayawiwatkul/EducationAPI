from django.contrib import admin
from .models import ListeningPracticeCategory, SpeakingPracticeCategory
from exercise.models import ListeningPractice, SpeakingPractice
from django.forms import BaseInlineFormSet

class ListeningInline(admin.TabularInline):
    model = ListeningPractice.category.through
    extra = 1

@admin.register(ListeningPracticeCategory)
class ListeningCategory(admin.ModelAdmin):
    inlines = [ListeningInline]

    list_display = ('title', 'code')
    search_fields = ('title', 'code')
    fields = ('title', 'image_url')


class SpeakingInline(admin.TabularInline):
    model = SpeakingPractice.category.through
    extra = 1

@admin.register(SpeakingPracticeCategory)
class SpeakingCategory(admin.ModelAdmin):
    inlines = [SpeakingInline]

    list_display = ('title', 'code')
    search_fields = ('title', 'code')
    fields = ('title', 'image_url')