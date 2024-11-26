# views_api.py
from rest_framework import viewsets, permissions
from .models import Film, Critique, Commentaire
from .serializers import FilmSerializer, CritiqueSerializer, UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CritiqueViewSet(viewsets.ModelViewSet):
    queryset = Critique.objects.all()
    serializer_class = CritiqueSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
