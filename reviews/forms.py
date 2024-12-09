from django import forms
from .models import Commentaire, Critique, Film

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'synopsis', 'genre', 'release_date', 'casting', 'duration', 'poster']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'synopsis': forms.Textarea(attrs={'class': 'form-control'}),
            'genre': forms.Select(attrs={'class': 'form-select'}),
            'release_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'casting': forms.TextInput(attrs={'class': 'form-control'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control'}),
            'poster': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class CritiqueForm(forms.ModelForm):
    class Meta:
        model = Critique
        fields = ['title', 'content', 'rating']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'min': 0, 'max': 5, 'class': 'form-control'}),
        }

    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if rating < 0 or rating > 5:
            raise forms.ValidationError('La note doit être comprise entre 0 et 5.')
        return rating

class FilmSearchForm(forms.Form):
    search_text = forms.CharField(required=False, label='Recherche', widget=forms.TextInput(attrs={'class': 'form-control'}))
    filter_type = forms.ChoiceField(
        choices=[
            ('titre', 'Titre'),
            ('genre', 'Genre'),
            ('release_date', 'Date Sortie'),
            ('average_rating', 'Note Moyenne')
        ],
        required=False,
        label='Critère de recherche',
        widget=forms.Select(attrs={'class': 'form-select'})
    )

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['texte']
        widgets = {
            'texte': forms.Textarea(attrs={'class': 'form-control'}),
        }
