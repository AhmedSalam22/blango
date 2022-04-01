from rest_framework import generics, viewsets
from blog.models import Post, Tag
from blog.api.permissions import AuthorModifyOrReadOnly, IsAdminUserForObject
from blango_auth.models import User
from blog.api.serializers import (
  PostSerializer,
  UserSerializer,
  PostDetailSerializer,
  TagSerializer,
)
from rest_framework.decorators import action
from rest_framework.response import Response


class TagViewSet(viewsets.ModelViewSet):
  queryset = Tag.objects.all()
  serializer_class = TagSerializer


  @action(methods=["get"], detail=True, name="Posts with the tag")
  def posts(self, request, pk=None):
    tag = self.get_object()
    post_serializer = PostSerializer(
      tag.posts, many=True, context={"request": request}
    )
    return Response(post_serializer.data)
    

class PostViewSet(viewsets.ModelViewSet):
  permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]
  queryset = Post.objects.all()

  def get_serializer_class(self):
    if self.action in ("list", "create"):
      return PostSerializer
    return PostDetailSerializer

# class PostList(generics.ListCreateAPIView):
#   queryset = Post.objects.all()
#   serializer_class = PostSerializer

# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#   permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]
#   queryset = Post.objects.all()
#   serializer_class = PostSerializer



class UserDetail(generics.RetrieveAPIView):
  lookup_field = 'email'
  queryset = User.objects.all()
  serializer_class = UserSerializer

# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]
#     queryset = Post.objects.all()
#     serializer_class = PostDetailSerializer
