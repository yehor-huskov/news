from rest_framework import serializers
from getpackage.models import Post 

class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, allow_blank=False, max_length=255)
    text = serializers.CharField(style={'base_template': 'textarea.html'})
    author = serializers.ForeginKey(settings.AUTH_USER_MODEL)
    date = serializers.DateTimeField()
    approved = serializers.BooleanField()

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        instance.date = validated_data.get('date', instance.date)
        instance.approved = validated_data.get('approved', instance.approved)
        instance.save()
        return instance



