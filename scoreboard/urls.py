from django.urls import path , re_path
from scoreboard.views import ScoreboardViewSet
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'scoreboard'

scoreboardViewSet = ScoreboardViewSet.as_view({
    'get': 'retrieve',
    'put': 'update'
})

# Enter URL path below
urlpatterns = format_suffix_patterns([
    path('<slug:code>', scoreboardViewSet, name='category-list'),
    ])