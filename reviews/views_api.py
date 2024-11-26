from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework import viewsets

from .models import Commentaire
from .models import Critique
from .models import Film
from .serializers import CritiqueSerializer
from .serializers import FilmSerializer
from .serializers import UserSerializer


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
