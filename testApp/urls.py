from django.urls import path
from .views import home, PostListAPIView, post_list, post_create

urlpatterns = [
    path("", home, name="home"),
    path("api/posts/", PostListAPIView.as_view(), name="api_posts"),

    path("test/list/", post_list, name="post_list"),
    path("test/create/", post_create, name="post_create"),
]