from django.urls import path

from .views import article, article_list

urlpatterns = [
    path("blog/articles", article_list, name="article_list"),
    path("blog/article/<int:pk>/", article, name="article_detail"),
]

app_name = "blog"
