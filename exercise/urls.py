from django.urls import path
from exercise.views import ExerciseViewSet
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'exercise'

exerciseSearchView = ExerciseViewSet.as_view({
    'get': 'search'
})

exerciseRetrieveView = ExerciseViewSet.as_view({
    'get': 'retrieve'
})

exerciseListView = ExerciseViewSet.as_view({
    'get': 'list'
})

# Enter URL path below
urlpatterns = format_suffix_patterns([
    path('type/<slug:practice_type>', exerciseListView, name='exercise'),
    path('search/', exerciseSearchView, name='exercise'),
    path('retrieve/<slug:code>', exerciseRetrieveView, name='exercise'),
])