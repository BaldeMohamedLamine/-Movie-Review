from django.urls import path, include
from rest_framework.routers import DefaultRouter
from reviews.views import (
    FilmListView, FilmDetailView, CritiqueCreateView, CritiqueDetailView,
    CritiqueUpdateView, CritiqueDeleteView, CommentaireCreateView,
    CommentUpdateView, CommentaireDeleteView
)
from reviews.views_api import FilmViewSet, CritiqueViewSet, UserViewSet

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
