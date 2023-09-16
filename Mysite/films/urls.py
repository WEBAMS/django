from django.urls import path
from . import views

urlpatterns = [
    path('', views.FilmsView.as_view()),
    path('<slug:slug>/', views.FilmDetail.as_view()),
    path('reviews/<int:pk>/', views.AddReview.as_view(), name='add_review')
]