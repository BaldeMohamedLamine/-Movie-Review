import logging

import pytest
from django.urls import reverse

logger = logging.getLogger(__name__)


@pytest.mark.django_db
def test_film_list_view(client, films_data):
    "Teste l'API de la vue FilmListView pour s'assurer qu'elle renvoie une liste paginée de films."

    url = reverse('film_list')
    response = client.get(url)

    assert response.status_code == 200
    assert len(response.context['films']) == 10


@pytest.mark.django_db
def test_film_list_filter_by_title(client, films_data):
    url = reverse('film_list')
    response = client.get(url)

    assert response.status_code == 200
    films = response.context['films']
    assert len(films) == 10
    assert response.context['films'][0].title == "Test film 0"


@pytest.mark.django_db
def test_film_list_view_filter_genre(client, films_data):
    response = client.get(reverse('film_list'), {'search_text': 'Genre Test', 'filter_type': 'genre'})
    assert response.status_code == 200
    assert len(response.context['films']) == 10


@pytest.mark.django_db
def test_film_list_view_filter_release_date(client, films_data):
    response = client.get(reverse('film_list'), {'search_text': '2024, 1, 1', 'filter_type': 'release_date'})
    assert response.status_code == 200
    assert len(response.context['films']) == 10


@pytest.mark.django_db
def test_film_list_view_filter_average_rating(client, films_data):
    response = client.get(reverse('film_list'), {'search_text': '3.0', 'filter_type': 'average_rating'})
    assert response.status_code == 200
    # assert len(response.context['films']) == 10
