from django.db.models import fields
from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ('post_title', 'post_content', 'post_category', 'post_tag', 'created_at', 'updated_at')