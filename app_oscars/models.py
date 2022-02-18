from django.db import models

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
        return self.title+", "+self.director
