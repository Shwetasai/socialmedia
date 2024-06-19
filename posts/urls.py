from django.urls import path
from .views import PostCreateAPIView,PostUpdateAPIView,PostDeleteAPIView,AddTagToPostView

urlpatterns = [
    path('create/', PostCreateAPIView.as_view(), name='post_create'),
    path('update/<int:id>/', PostUpdateAPIView.as_view(), name='post_update'),
    path('delete/<int:id>/', PostDeleteAPIView.as_view(), name='post_delete'),
    path('add_tag/<int:id>/', AddTagToPostView.as_view(), name='add-tag-to-post'),
]