from django.urls import path
from .views import PostListView, PostDetailView

urlpatterns = [
    path("posts", PostListView.as_view()),
    path("posts/<str:pk>", PostDetailView.as_view())
]
