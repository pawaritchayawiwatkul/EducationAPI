from django.urls import path , re_path
from core.views import ProfileViewSet
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'core'

profileView = ProfileViewSet.as_view({
    'put': 'update',
    'get': 'retrieve'
})

# Enter URL path below
urlpatterns = format_suffix_patterns([
    path('profile', profileView, name='profile'),
    ])