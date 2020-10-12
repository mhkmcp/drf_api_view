from django.urls import path
from blogs import views

urlpatterns = [
    path('fbv/', views.blog_view),
    path('apiview/', views.BlogAPIView.as_view()),
]