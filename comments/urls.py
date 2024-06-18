
from django.urls import path
from .views import CommentCreateView, ReplyCreateView

urlpatterns = [
    path('<int:post_id>/comments/', CommentCreateView.as_view(), name='comment-create'),
    path('<int:comment_id>/replies/', ReplyCreateView.as_view(), name='reply-create'),
]
