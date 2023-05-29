from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.user_list, name="user_list"),
    path("<int:pk>/", views.user_detail, name="user_detail"),
]
