from django.urls import path

from api.views import *

urlpatterns = [
    path('users/', UserListView.as_view()),
    path('posts/', PostListView.as_view()),
    path('comments/', CommentList.as_view()),
    path('category/', CategoryList.as_view()),
    path('users/<int:pk>/', UserDetailView.as_view()),
    path('posts/<int:pk>/', PostDetailView.as_view()),
    path('comments/<int:pk>/', CommentDetail.as_view()),
    path('category/<int:pk>/', CategoryDetail.as_view()),
    path('logout/', LogoutAPIView.as_view()),
    path('post_list/', PostList.as_view()),
]
