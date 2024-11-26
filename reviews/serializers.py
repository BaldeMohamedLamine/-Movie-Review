from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Commentaire
from .models import Critique
from .models import Film


User = get_user_model()


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['id', 'title', 'synopsis', 'genre', 'release_date', 'casting', 'duration', 'poster', 'average_rating']


class CritiqueSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Critique
        fields = ['id', 'film', 'user', 'title', 'content', 'rating', 'published_date', 'last_updated']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name']
