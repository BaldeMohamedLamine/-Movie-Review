import pytest
import datetime
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from django.core.files.uploadedfile import SimpleUploadedFile
from reviews.models import Film

@pytest.fixture
def api_client():
    return APIClient

@pytest.fixture
def films_data():

    poster_file = SimpleUploadedFile(
        name='poster.jpg', 
        content=b'fake image content', 
        content_type='image/jpeg'
    )
    films = [
        Film.objects.create(
            title = f"Test film {i}",
            synopsis = f"Une description du {i} film",
            genre = 'Genre Test',
            release_date=datetime.date(2024, 1, 1),
            casting="Acteur principal",
            duration=90,
            average_rating = i % 5 + 1,
            poster=poster_file
        )
        for i in range(10)
    ]
    return films

