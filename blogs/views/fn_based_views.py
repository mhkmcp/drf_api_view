
from rest_framework.response import Response
from rest_framework.decorators import api_view

from blogs.models import BlogModel
from blogs.serializers import BlogModelSerializer


@api_view(['GET', 'POST'])
def blog_view(request):
    if request.method == 'GET':
        blogs = BlogModel.objects.all()
        serializer = BlogModelSerializer(blogs, many=True)

        return Response({
            'success': True,
            'message': 'Get request fulfilled!',
            'data': serializer.data
        })
    elif request.method == 'POST':
        # blog = request.data
        # serializer = BlogModelSerializer(blog, many=False)
        return Response({
            'success': True,
            'message': 'Post request fulfilled!',
            'data': request.data
        })
    return Response({
        'success': False,
        'message': 'Invalid Request!',
        'data': ''
    })
