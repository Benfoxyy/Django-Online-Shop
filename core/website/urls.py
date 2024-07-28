from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('home/', views.IndexView.as_view()),
]
