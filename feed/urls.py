from django.urls import path

from . import views

# used for namespacing
app_name = "feed"

urlpatterns = [
    path("", views.HomePage.as_view(), name="index.html"),
    path("feed/post", views.AddPost.as_view(), name="post.html")
]
