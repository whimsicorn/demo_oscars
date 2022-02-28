from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator



class Films(models.Model):
    COUNTRIES = [
        ('US','Stany Zjednoczone'),
        ('GB',"Wielka Brytania"),
        ('JP','Japonia'),
    ]
    title = models.CharField(max_length=40,default="", blank=True)
    polish_title = models.CharField(max_length=40,default="", blank=True)
    director = models.CharField(max_length=30,default="", blank=True)
    year = models.PositiveSmallIntegerField(null=True, blank=True)
    country = models.CharField(max_length=2, choices=COUNTRIES, default='US')
    description = models.TextField(max_length=500,default="Film oskarowy", blank=True)
    poster = models.ImageField(upload_to='posters', null=True,blank=True)

    def __str__(self):
        return self.polish_title+" ("+self.title+") "+", "+self.director



class Our_rating(models.Model):
    review = models.TextField(default="", blank=True)
    points = models.DecimalField (default=0.0, decimal_places=1, max_digits=3,
                    validators=[
                        MaxValueValidator(10.0),
                        MinValueValidator(0.0)
                    ]
                                       )
    film = models.ForeignKey(Films, on_delete=models.CASCADE)
    #user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)

