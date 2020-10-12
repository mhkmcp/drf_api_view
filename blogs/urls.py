from django.urls import path
from blogs import views

urlpatterns = [
    # blogs/fbv
    path('fbv/', views.blog_view),
    # blogs/apiview
    path('apiview/', views.BlogAPIView.as_view()),
    # blogs/generics
    path('generics/', views.BlogListCreateAPIView.as_view()),
    path('generics/<int:pk>/', views.BlogRetrieveUpdateDestroyAPIView.as_view()),
]