from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import *
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.


class Home(CreateView):
    form_class = EmailForm
    model = Email
    template_name = "animals/home.html"
    success_url = reverse_lazy('home')

# @login_required(login_url='/members/login/')


class CreatePet(CreateView):
    form_class = CreatePetForm
    template_name = "animals/addPet.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PetDetail(DetailView):
    model = Pet
    template_name = "animals/pet.html"

    def get_context_data(self, *args, **kwargs):
        adoptedPets = AdoptedPets.objects.all()
        context = super(PetDetail, self).get_context_data(
            *args, **kwargs)

        pet = get_object_or_404(Pet, id=self.kwargs['pk'])

        context['is_adopted'] = False
        
        for adopt in adoptedPets:
            if adopt.pet.pk == pet.pk:
                context['is_adopted'] = True
                context['adopt_pet'] = adopt

        return context


def Adopt(req, pet, logUser, owner):
    print(pet)
    print(logUser)
    print(owner)
    pet_s = get_object_or_404(Pet, id=pet)
    adopter_s = get_object_or_404(User, id=logUser)
    owner_s = get_object_or_404(User, id=owner)
    print(pet_s)
    print(adopter_s)
    print(owner_s)
    adopt = AdoptedPets(pet=pet_s)
    adopt.save()
    adopt.adopter.add(adopter_s)
    adopt.owner.add(owner_s)

    return HttpResponseRedirect(reverse('pet', args=[str(pet)]))


def Delete(req, pet, cn):
    print(pet)
    if req.user.pk == cn or req.user.is_staff:
        print(pet)
        Pet.objects.filter(pk=pet).delete()
    return HttpResponseRedirect(reverse('active_user', args=[str(cn)]))


def verificare(category):
    return category != 'any' and category is not None


def filterPets(req):
    petss = Pet.objects.all()
    tip = req.GET.get("tip")
    age = req.GET.get("age")
    breed = req.GET.get("breed")
    take_care = req.GET.get("take_care")
    gender = req.GET.get("gender")
    size = req.GET.get("size")
    orderby = req.GET.get("orderby")

    if verificare(tip):
        petss = petss.filter(animal=tip)

    if breed == 'on':
        petss = petss.filter(de_rasa=True)
    else:
        print(breed)

    if verificare(age):
        petss = petss.filter(age=age)

    if verificare(take_care):
        petss = petss.filter(take_care=take_care)

    if verificare(size):
        petss = petss.filter(size=size)

    if verificare(gender):
        petss = petss.filter(gender=gender)

    # if verificare(orderby):
    #     if orderby == 'old':
    #         petss = petss.order_by('id')
    #     elif orderby == 'new':
    #         petss = orderby('-id')

    return petss


def Pets(req):
    petss = filterPets(req)

    context = {
        "pets": petss.order_by('-id')
    }
    return render(req, 'animals/pets.html', context)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# update_or_create