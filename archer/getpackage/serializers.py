from rest_framework import serializers
from getpackage.models import Post 

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'author', 'date', 'approved')
