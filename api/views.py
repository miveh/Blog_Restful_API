from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, \
    GenericAPIView
from rest_framework import permissions
from rest_framework.response import Response

# from .permissions import IsOwnerOrReadOnly
from .models import Post, Comment, Category, CustomUser
from .serializer import UserSerializer, PostSerializer, CommentSerializer, CategorySerializer


# Create your views here.
# User views
class UserListView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


# User detail
class UserDetailView(RetrieveAPIView):
    queryset = CustomUser.objects.all()
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
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


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
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


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
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


class LogoutAPIView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def logout(self, request):
        request.user.auth_token.delete()
        return Response(data={"message": f"Good by {self.user.username}"})


@method_decorator(csrf_exempt, name='dispatch')
class PostList(PermissionRequiredMixin, ListView):
    model = Post
    permission_required = ['api.can_hide_post']
    template_name = 'post_list.html'
