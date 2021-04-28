from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from animals.models import *
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


# Create your views here.


def admin(req):
    users = User.objects.all()
    pets = Pet.objects.all()
    emails = Email.objects.all()
    adopt = AdoptedPets.objects.all()

    context = {
        'users': users,
        "pets": pets,
        "emails": emails,
        "adopt": adopt,
    }
    return render(req, 'admin/admin.html', context)


def deleteUser(req, pk):
    user = get_object_or_404(User, id=pk)
    user.delete()

    return HttpResponseRedirect(reverse('admin'))

    # return reverse_lazy('admin')


def deleteEmail(req, pk):
    email = get_object_or_404(Email, id=pk)
    email.delete()

    return HttpResponseRedirect(reverse('admin'))
    


def deleteAdoptedPet(req, pk, pet):
    adopted = get_object_or_404(AdoptedPets, id=pk)
    pet = get_object_or_404(Pet, id=pet)

    print(adopted)
    print(pet)

    adopted.delete()
    pet.delete()

    return HttpResponseRedirect(reverse('admin'))
    
