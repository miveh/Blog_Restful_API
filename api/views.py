from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, \
    GenericAPIView
from rest_framework import permissions
from rest_framework.response import Response

from .permissions import IsOwnerOrReadOnly
from .models import Post, Comment, Category
from .serializer import UserSerializer, PostSerializer, CommentSerializer, CategorySerializer


# Create your views here.
# User views
class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# User detail
class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# post list
class PostListView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # کسی پست هارو میبینه که حتما لاگین باشه
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# post detail
class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


class CommentList(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # کسی پست هارو میبینه که حتما لاگین باشه
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


class CategoryList(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # کسی پست هارو میبینه که حتما لاگین باشه
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CategoryDetail(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


class LogoutAPIView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def logout(self, request):
        request.user.auth_token.delete()
        return Response(data={"message": f"Good by {self.user.username}"})
