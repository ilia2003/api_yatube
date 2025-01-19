from rest_framework import serializers
from posts.models import Post, Group, Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['all']


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = ['all']


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['all']
