from getpackage.models import Post 

from rest_framework import viewsets

from django.contrib.auth.models import User, Group

from getpackage.serializers import PostSerializer, JournalistPostSerializer
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

    def get_serializer_class(self):
        editor_group = Group.objects.get(name='editor')
        if editor_group in self.request.user.groups.all():
            return PostSerializer
        return JournalistPostSerializer 

class PostOne(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsAuthorOrReadOnly)

    def get_serializer_class(self):
        editor_group = Group.objects.get(name='editor')
        if editor_group in self.request.user.groups.all():
            return PostSerializer
        return JournalistPostSerializer  
   
class UserAll(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserOne(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

