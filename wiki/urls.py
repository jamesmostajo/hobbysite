from django.urls import path

from .views import article, article_list

urlpatterns = [
    path("wiki/articles", article_list, name="article_list"),
    path("wiki/article/<int:pk>/", article, name="article_detail"),
]

app_name = "merchstore"
