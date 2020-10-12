from .models import BlogModel
from rest_framework import serializers
# import Serializer, ModelSerializer


class BlogModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = '__all__'

