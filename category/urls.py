from django.urls import path , re_path
from category.views import CategoryViewSet
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'category'

categoryDetailView = CategoryViewSet.as_view({
    'get': 'retrieve'
})

categoryListView = CategoryViewSet.as_view({
    'get': 'list'
})
# Enter URL path below
urlpatterns = format_suffix_patterns([
    path('type/<slug:category_type>', categoryListView, name='category-list'),
    path('retrieve/<slug:code>', categoryDetailView, name='category-detail'),
])