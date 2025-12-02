from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status
from django.shortcuts import get_object_or_404
from .models import BlogPost
from .serlializers import BlogPostSerializer

@api_view(['POST'])
def add_post(request):
    post = BlogPostSerializer(data=request.data)

    if post.is_valid():

        title = post.validated_data.get('post_title')
        if BlogPost.objects.filter(post_title=title).exists():
            return Response(
                {"error:" "This post already exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        post.save()
        return Response(post.data, status=status.HTTP_201_CREATED)
    
    return Response(post.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def view_posts(request):

    if request.query_params:
        posts = BlogPost.objects.filter(**request.query_params.dict())
    else:
        posts = BlogPost.objects.all()

    if posts:
        serializer = BlogPostSerializer(posts, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def search_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    serializer = BlogPostSerializer(post)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT', 'DELETE'])
def post_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)

    if request.method == 'PUT':
        serializer = BlogPostSerializer(instance=post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    if request.method == 'DELETE':
        post.delete()
        return Response({"message": "Deleted"}, status=204)

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_posts': '/',
        'Search by pk': '/search/pk',
        'Add': '/posts',
        'Update': '/posts/pk',
        'Delete': '/posts/pk'
    }

    return Response(api_urls)