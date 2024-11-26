from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from reviews.views import CommentaireCreateView
from reviews.views import CommentaireDeleteView
from reviews.views import CommentUpdateView
from reviews.views import CritiqueCreateView
from reviews.views import CritiqueDeleteView
from reviews.views import CritiqueDetailView
from reviews.views import CritiqueUpdateView
from reviews.views import FilmDetailView
from reviews.views import FilmListView
from reviews.views_api import CritiqueViewSet
from reviews.views_api import FilmViewSet
from reviews.views_api import UserViewSet


router = DefaultRouter()
router.register(r'films', FilmViewSet)
router.register(r'critiques', CritiqueViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('films/', FilmListView.as_view(), name='film_list'),
    path('films/<int:pk>/', FilmDetailView.as_view(), name='film_detail'),

    path('films/<int:pk>/add-critique/', CritiqueCreateView.as_view(), name='add_critique'),
    path('critiques/<int:pk>/', CritiqueDetailView.as_view(), name='critique_detail'),
    path('critiques/<int:pk>/edit/', CritiqueUpdateView.as_view(), name='edit_critique'),
    path('critiques/<int:pk>/delete/', CritiqueDeleteView.as_view(), name='delete_critique'),

    path('critiques/<int:critique_id>/add-comment/', CommentaireCreateView.as_view(), name='add_comment'),
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='edit_comment'),
    path('comments/<int:pk>/delete/', CommentaireDeleteView.as_view(), name='delete_comment'),

    path('api/', include(router.urls)),
]
