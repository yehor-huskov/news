from getpackage.models import Post 

from rest_framework import viewsets

from django.contrib.auth.models import User

from getpackage.serializers import PostSerializer
from getpackage.serializers import UserSerializer
from getpackage.permissions import IsAuthorOrReadOnly

from rest_framework import generics, permissions

class PostApproved(generics.ListAPIView):
    queryset = Post.objects.filter(approved=True)
    serializer_class = PostSerializer

class PostAll(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostOne(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsAuthorOrReadOnly)
   
class UserAll(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserOne(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

