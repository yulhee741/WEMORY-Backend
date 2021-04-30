from django.urls import path
from . import views

app_name = "diary"

urlpatterns = [
    path('diaries/', views.diary_list, name='diary-read'),
]
