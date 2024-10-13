from rest_framework import serializers
from .models import Discussion, Comment

class CommentSerializer(serializers.ModelSerializer):

    created_by = serializers.ReadOnlyField(source='created_by.username')
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'discussion', 'content', 'created_by', 'created_at', 'updated_at', 'parent_comment', 'replies')
        read_only_fields = ('created_by', 'discussion')

    def get_replies(self, obj):
        if obj.replies.exists():
            return CommentSerializer(obj.replies.all(), many=True).data
        return []


class DiscussionSerializer(serializers.ModelSerializer):

    created_by = serializers.ReadOnlyField(source='created_by.username')
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Discussion
        fields = ('id', 'course', 'title', 'content', 'created_by', 'created_at', 'updated_at', 'comments')
        read_only_fields = ['created_by', 'course']