from rest_framework.views import APIView
from rest_framework.response import Response

from blogs.models import BlogModel
from blogs.serializers import BlogModelSerializer


class BlogAPIView(APIView):
    '''
    Similar to Django View Class
    '''

    def get(self, request):
        blogs = BlogModel.objects.all()
        serializer = BlogModelSerializer(blogs, many=True)
        return Response({
            'success': True,
            'message': 'APIView Get request fulfilled!',
            'data': serializer.data
        })

    def post(self, request, *args, **kwargs):
        if request.data.get('title') != '':
            serializer = BlogModelSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'success': True,
                    'message': 'APIView Post request fulfilled!',
                    'data': serializer.data
                })

    def put(self, request, *args, **kwargs):
        if request.data.get('id') is not None:
            blog = BlogModel.objects.get(pk=request.data.get('id'))
            if blog:
                serializer = BlogModelSerializer(blog, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({
                        'success': True,
                        'message': 'APIView Updated blog',
                        'data': serializer.data
                    })
            return Response({
                'success': True,
                'message': 'APIView put request fulfilled!',
                'data': ''
            })

    def delete(self, request, *args, **kwargs):
        if request.data.get('id') is not None:
            blog = BlogModel.objects.get(pk=request.data.get('id'))
            if blog:
                blog.delete()
                return Response({
                    'success': True,
                    'message': 'APIView deleted blog',
                })
        return Response({
            'success': True,
            'message': 'APIView Delete request fulfilled!',
            'data': ''
        })


