from django.urls import path

from .views import comment_detail, comment_list

urlpatterns = [
    path("commissions/list", comment_list, name="comment_list"),
    path("commissions/detail/<int:pk>/", comment_detail, name="comment_detail"),
]

app_name = "commissions"
