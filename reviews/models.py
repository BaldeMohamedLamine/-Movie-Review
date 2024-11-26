from django.db import models

from users.models import User


class Film(models.Model):
    title = models.CharField(max_length=255)
    synopsis = models.TextField()
    genre = models.CharField(max_length=50, choices=[
        ('Action', 'Action'),
        ('Drama', 'Drama'),
        ('Comedy', 'Comedy'),
        ('Horror', 'Horror'),
    ])
    release_date = models.DateField()
    casting = models.TextField(help_text="Liste des acteurs principaux")
    duration = models.PositiveIntegerField(help_text="Durée en minutes")
    poster = models.ImageField(upload_to='posters/', null=True, blank=True)
    average_rating = models.FloatField(default=0, editable=False)

    def update_average_rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            self.average_rating = sum(review.rating for review in reviews) / reviews.count()
        else:
            self.average_rating = 0
        self.save()

    def __str__(self):
        return self.title


class Critique(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    rating = models.PositiveIntegerField()
    published_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.film.update_average_rating()

    def __str__(self):
        return f"{self.title} - {self.user.username}"


class Commentaire(models.Model):
    critique = models.ForeignKey(Critique, on_delete=models.CASCADE, related_name='commentaires')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    texte = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commentaire de {self.user.username} sur {self.critique}"
