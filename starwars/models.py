from django.db import models


class Character(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Photo = models.ImageField(upload_to='media/', blank=True, null=True)
    Side_choices = (
        ('0', 'Dark Side'),
        ('1', 'Light Side'),

    )
    Side = models.CharField(max_length=100, choices=Side_choices, default="Dark Side")
    Job = models.CharField(max_length=100, null=True, blank=True)
    Race_choices = (
        ('Whill', 'Whill'),
        ('Human', 'Human'),
        ('Kaleesh', 'Kaleesh'),
        ('Cyborg', 'Cyborg'),
        ('Zabrak', 'Zabrak'),
        ('Korun', 'Korun'),
        ('Droid', 'Droid'),
        ('Clone', 'Clone'),
        ('Kel Dor', 'Kel Dor'),
        ('Wookiee', 'Wookiee'),
        ('Hutt', 'Hutt'),
    )
    Race = models.CharField(max_length=100, choices=Race_choices, default="Human")
    Text=models.TextField(max_length=5000, null=True, blank=True)
    def __str__(self):
        return self.Name

class Movie(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Photo = models.ImageField(upload_to='media', blank=True, null=True)
    DirectorName =models.CharField(max_length=100, null=True, blank=True)
    TrailerLink = models.URLField(max_length=200, null=True, blank=True)
    Year = models.DateField()
    ImdbPoint =models.CharField(max_length=10,null=True, blank=True)
    Charecters = models.ManyToManyField(Character)
    Type_choices=(
        ('0','Movie'),
        ('1','Cartoon'),
    )
    Type = models.CharField(max_length=100, choices=Type_choices, default="Human")

    def __str__(self):
        return self.Name


class Game(models.Model):
    Name =models.CharField(max_length=100,null=True, blank=True)
    Photo = models.ImageField(upload_to='media', blank=True,null=True)
    Year = models.DateField()
    GamePage= models.URLField(max_length=200,null=True, blank=True)
    VideoLink = models.URLField(max_length=200,null=True, blank=True)
    Publisher = models.CharField(max_length=100,null=True, blank=True)

    def __str__(self):
        return self.Name

