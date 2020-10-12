from rest_framework import generics
from rest_framework.response import Response
from blogs.models import BlogModel
from blogs.serializers import BlogModelSerializer


class BlogListCreateAPIView(generics.ListCreateAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogModelSerializer


class BlogRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogModelSerializer
