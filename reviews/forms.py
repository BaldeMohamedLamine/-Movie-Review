from django import forms
from .models import Critique,Commentaire

class CritiqueForm(forms.ModelForm):
    class Meta:
        model = Critique
        fields = ['title', 'content', 'rating']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 0, 'max': 5, 'class': 'form-control'}), 
        }

    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if rating < 0 or rating > 5:
            raise forms.ValidationError('La note doit être comprise entre 0 et 5.')
        return rating
        

class FilmSearchForm(forms.Form):
    search_text = forms.CharField(required=False, label='Recherche')
    filter_type = forms.ChoiceField(
        choices=[
            ('titre', 'Titre'),
            ('genre', 'Genre'),
            ('release_date', 'Date Sortie'),
            ('average_rating', 'Note Moyenne')

        ],
        required=False,
        label='Critère de recherche'
    )

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['texte']
        