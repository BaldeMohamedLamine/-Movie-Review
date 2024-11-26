from django.test import TestCase
from datetime import date
from django.utils import timezone
from reviews.models import Film,Critique,Commentaire
from users.models import User
class FilmModelTest(TestCase):
    def setUp(self):
        
        self.film = Film.objects.create(
            title = 'Inception',
            synopsis = 'A thief with the ability to enter peoples dreams takes on a final mission.',
             genre="Action",
            release_date=date(2010, 7, 16),
            casting="Leonardo DiCaprio, Ellen Page",
            duration=148,
        )

        self.user1 = User.objects.create(
        email='baldelenz@gmail.com',
        first_name='Balde',
        last_name='Lamine',
        date_inscription=timezone.now(),
        date_joined=timezone.now(),
    ) 
        self.user2 = User.objects.create(
        email='mohamedlaminebalde392@gmail.com',
        first_name='Balde',
        last_name='Lamine',
        date_inscription=timezone.now(),
        date_joined=timezone.now(),
    ) 
    #Vérifie que le film est correctement créé
    def test_film_creation(self):
        film = Film.objects.get(title = 'Inception')
        self.assertEqual(film.synopsis,'A thief with the ability to enter peoples dreams takes on a final mission.')
        self.assertEqual(film.genre,'Action')
        self.assertEqual(film.average_rating, 0)

    def test_update_average_rating_with_reviews(self):

        "Vérifie la mise à jour de la moyenne des notes avec des critiques"
        Critique.objects.create(film = self.film, user = self.user1,title = 'Great movie',content='Loved it!',rating=4)
        Critique.objects.create(film = self.film,user=self.user2,title='Awesome',content= 'Amazing visuals!',rating=5)
    
        self.film.update_average_rating()
        self.assertEqual(self.film.average_rating,4.5)
    
    def test_update_average_rating_no_reviews(self):

        "Vérifie que la moyenne reste à 0 si le film n'a pas de critiques"

        self.film.update_average_rating()
        self.assertEqual(self.film.average_rating,0)

class ModelCritiqueTest(TestCase):
    
    def setUp(self):
        self.film = Film.objects.create(
            title="Inception",
            synopsis="A thief with the ability to enter people's dreams takes on a final mission.",
            genre="Action",
            release_date=date(2010, 7, 16),
            casting="Leonardo DiCaprio, Ellen Page",
            duration=148,
        )
        self.user = User.objects.create(email="user@example.com", first_name="User", last_name="Test")

    def test_critique_creation(self):
        
        'Vérifie que la critique est correctement créée'
        critique = Critique.objects.create(
            film = self.film,
            user = self.user,
            title = 'Fantastic Movie',
            content = 'This movie was fantastic from start to finish!',
            rating = 5
        )

        self.assertEqual(critique.film,self.film)
        self.assertEqual(critique.user,self.user)
        self.assertEqual(critique.title,'Fantastic Movie')
        self.assertEqual(critique.rating,5)

    def test_critique_auto_timestamps(self):

        'Vérifie que les champs `published_date` et `last_updated` sont bien remplis automatiquement.'
        critique = Critique.objects.create(
            film = self.film,
            user = self.user,
            title = 'Fantastic Movies',
            content = 'This movie was fantastic from start to finish!',
            rating = 5
        )

        self.assertIsNotNone(critique.published_date)
        self.assertIsNotNone(critique.last_updated)
        
class CommentaireModelTest(TestCase):

    def setUp(self):
        self.critique = Critique.objects.create(
            film=self.film,
            user=self.user,
            rating=5,
            title="Amazing Movie",
            content="This was a fantastic movie!"
        )
        self.user = User.objects.create(email="user@example.com", first_name="Test", last_name="User")

        def test_commentaire_creation(self):

            "Vérifie que le commentaire est correctement créé et lié à une critique et un utilisateur"
            commentaire = Commentaire.objects.create(
            critique=self.critique,
            user=self.user,
            texte="Je suis d'accord avec cette critique !"
        )
        
            self.assertEqual(commentaire.critique, self.critique) 
            self.assertEqual(commentaire.user, self.user)
            self.assertEqual(commentaire.texte, "Je suis d'accord avec cette critique !")
            


    