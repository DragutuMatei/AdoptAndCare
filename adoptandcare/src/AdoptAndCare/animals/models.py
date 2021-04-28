from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    adresa = models.CharField(max_length=400)
    imag = models.ImageField( )
    phone = models.CharField(   max_length=12)
    media = models.CharField(  max_length=80)

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("home")
    # , kwargs={"pk": self.pk}


class Email(models.Model):
    email_from = models.EmailField(max_length=100)
    message = models.TextField(max_length=900)

    def __str__(self):
        return self.message


class Pet(models.Model):

    class AnimalCh(models.TextChoices):
        DOG = 'dog', _('Dog')
        CAT = 'cat', _('Cat')
        PARROT = 'parrot', _('Parrot')
        FISH = 'fish', _('Fish')
        HAMSTER = 'hamster', _('Hamster')
        LIZARD = 'lizard', _('Lizart')
        SNAKE = 'snake', _('Snake')

    class AgeCh(models.TextChoices):
        BABY = 'Baby (0 - 12 months)', _('Baby (0 - 12 months)')
        YOUNG = 'Young (12 - 30 months)', _('Young (12 - 30 months)')
        MEDIUM = 'Medium (30-60 months)', _('Medium (30-60 months)')
        OLD = 'Old (60-90 months)', _('Old (60-90 months)')
    
    class CareCh(models.TextChoices):
        EAZY = 'Eazy', _('Eazy')
        MEDIUM = 'Medium', _('Medium')
        HARD = 'Hard', _('Hard')

    class SizeCh(models.TextChoices):
        SMALL = 'Small ( < 1 kg)', _('Small ( < 1 kg)')
        MEDIUM = 'Medium ( < 3 kg)', _('Medium ( < 3 kg)')
        BIG = 'Big ( > 3 kg)', _('Big ( > 3 kg)')

    class GenderCh(models.TextChoices):
        MALE = "Male", _('Male')
        FEMALE = "Female", _('Female')


    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    imag1 = models.ImageField(blank=True, null=True)
    imag2 = models.ImageField(blank=True, null=True)
    imag3 = models.ImageField(blank=True, null=True)
    imag4 = models.ImageField(blank=True, null=True)
    imag5 = models.ImageField(blank=True, null=True)

    animal = models.CharField( choices=AnimalCh.choices, default=AnimalCh.DOG, max_length=200, blank=False, null=False)
    age = models.CharField(choices=AgeCh.choices, default=AgeCh.BABY, max_length=50, blank=False, null=False)
    de_rasa = models.BooleanField(default=False, blank=False, null=False)
    take_care = models.CharField(choices=CareCh.choices, default=CareCh.EAZY, max_length=100, blank=False, null=False)
    size = models.CharField(choices= SizeCh.choices, default=SizeCh.SMALL, max_length=100, blank=False, null=False)
    gender = models.CharField(choices=GenderCh.choices, default=GenderCh.MALE,  max_length=10)
    date = models.DateTimeField(auto_now_add=True)
    condition = models.IntegerField(default=8)

    def __str__(self):
        return self.name
    


class AdoptedPets(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    adopter = models.ManyToManyField(User, blank=False, related_name="adopter", unique=False)
    owner = models.ManyToManyField(User, blank=False, related_name="owner", unique=False)

    
