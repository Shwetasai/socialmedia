from django.urls import path
from .views import PostCreateAPIView,PostUpdateAPIView,PostDeleteAPIView,AddTagToPostView

urlpatterns = [
    path('create/', PostCreateAPIView.as_view(), name='post_create'),
    path('update/<int:id>/', PostUpdateAPIView.as_view(), name='post_update'),
    path('<int:id>/delete/', PostDeleteAPIView.as_view(), name='post_delete'),
    path('<int:pk>/add_tag/', AddTagToPostView.as_view(), name='add-tag-to-post'),
]