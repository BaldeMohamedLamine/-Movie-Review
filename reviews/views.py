from datetime import datetime

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from .forms import CommentaireForm
from .forms import CritiqueForm
from .forms import FilmSearchForm
from .forms import FilmForm
from .models import Commentaire
from .models import Critique
from .models import Film


# Liste des films avec filtres
class FilmListView(ListView):
    model = Film
    template_name = 'movies/film_list.html'
    context_object_name = 'films'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('title')
        form = FilmSearchForm(self.request.GET)
        if form.is_valid():
            search_text = form.cleaned_data.get('search_text')
            filter_type = form.cleaned_data.get('filter_type')
            if search_text:
                if filter_type == 'titre':
                    queryset = queryset.filter(title__icontains=search_text)
                elif filter_type == 'genre':
                    queryset = queryset.filter(genre__icontains=search_text)
                elif filter_type == 'release_date':
                    try:
                        search_date = datetime.strptime(search_text, '%Y, %m, %d')
                        queryset = queryset.filter(release_date__year=search_date.year)
                    except ValueError:
                        queryset = queryset.none()
                elif filter_type == 'average_rating':
                    queryset = queryset.filter(average_rating__gte=search_text)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FilmSearchForm(self.request.GET)
        return context

class FilmCreateView(LoginRequiredMixin, CreateView):
    model = Film
    form_class = FilmForm
    template_name = 'movies/add_film.html'

    def form_valid(self, form):
        messages.success(self.request, "Film ajouté avec succès.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('film_list')


# Page détaillée d'un film avec critiques
class FilmDetailView(DetailView):
    model = Film
    template_name = 'movies/film_detail.html'
    context_object_name = 'film'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        film = self.object
        context['critiques'] = film.reviews.all()
        context['has_reviewed'] = film.reviews.filter(user=self.request.user).exists()
        return context
class FilmUpdateView(LoginRequiredMixin, UpdateView):
    model = Film
    form_class = FilmForm
    template_name = 'movies/edit_film.html'

    def get_success_url(self):
        messages.success(self.request, "Film modifié avec succès.")
        return reverse_lazy('film_detail', kwargs={'pk': self.object.pk})

class FilmDeleteView(LoginRequiredMixin, DeleteView):
    model = Film
    template_name = 'movies/delete_film.html'

    def get_success_url(self):
        messages.success(self.request, "Film supprimé avec succès.")
        return reverse_lazy('film_list')

# Ajouter une critique
class CritiqueCreateView(LoginRequiredMixin, CreateView):
    model = Critique
    form_class = CritiqueForm
    template_name = 'movies/add_critique.html'

    def dispatch(self, request, *args, **kwargs):
        film = get_object_or_404(Film, id=self.kwargs['film_id'])
        if Critique.objects.filter(film=film, user=request.user).exists():
            critique = Critique.objects.get(film=film, user=request.user)
            messages.info(request, "Vous avez déjà publié une critique pour ce film.")
            return redirect('critique_update', pk=critique.pk)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.film = get_object_or_404(Film, id=self.kwargs['film_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('film_detail', kwargs={'pk': self.object.film.id})


# Modifier une critique
class CritiqueUpdateView(LoginRequiredMixin, UpdateView):
    model = Critique
    form_class = CritiqueForm
    template_name = 'movies/edit_critique.html'

    def get_queryset(self):
        return Critique.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse_lazy('film_detail', kwargs={'pk': self.object.film.id})


# Supprimer une critique
class CritiqueDeleteView(LoginRequiredMixin, DeleteView):
    model = Critique
    template_name = 'movies/delete_critique.html'

    def get_queryset(self):
        return Critique.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse_lazy('film_detail', kwargs={'pk': self.object.film.id})


# Détails d'une critique avec commentaires
class CritiqueDetailView(DetailView):
    model = Critique
    template_name = 'movies/critique_detail.html'
    context_object_name = 'critique'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['commentaires'] = Commentaire.objects.filter(critique=self.object)
        return context


# Ajouter un commentaire
class CommentaireCreateView(LoginRequiredMixin, CreateView):
    model = Commentaire
    form_class = CommentaireForm
    template_name = 'movies/add_comment.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.critique = get_object_or_404(Critique, id=self.kwargs['critique_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('critique_detail', kwargs={'pk': self.object.critique.id})


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Commentaire
    form_class = CommentaireForm
    template_name = 'movies/edit_comment.html'

    def get_queryset(self):
        return Commentaire.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse_lazy('critique_detail', kwargs={'pk': self.object.critique.id})


# Supprimer un commentaire (pour admin/modération)
class CommentaireDeleteView(LoginRequiredMixin, DeleteView):
    model = Commentaire
    template_name = 'movies/delete_comment.html'

    def get_queryset(self):
        if self.request.user.is_staff:
            return Commentaire.objects.all()
        return Commentaire.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse_lazy('critique_detail', kwargs={'pk': self.object.critique.id})


def custom_404_view(request, exception=None):
    return render(request, 'moviews/404.html', status=404)


def custom_500_view(request, exception=None):
    return render(request, 'moviews/500.html', status=500)
