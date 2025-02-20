from rest_framework import status, mixins, generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly

class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    @action(detail=True, renderer_classes = [renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlited)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset =  User.objects.all()
    serializer_class = UserSerializer

# Create your views here.
