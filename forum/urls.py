from django.urls import path

from .views import post, post_list

urlpatterns = [
    path("forum/threads", post_list, name="post_list"),
    path("forum/thread/<int:pk>/", post, name="post_detail"),
]

app_name = "forum"
