from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.viewsets import ModelViewSet
from .permissions import IsAuthorOrReadOnly
from .serializers import BlogSerializer
from posts.models import Post
# Create your views here.

class ListViewSets(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthorOrReadOnly]



# class ListPost(ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = BlogSerializer
#
# class RetrievePost(RetrieveUpdateAPIView):
#     permission_classes = (IsAuthorOrREadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = BlogSerializer