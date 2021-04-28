from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('donate_pet/', CreatePet.as_view(), name="addPet"),
    path('pets/<int:pk>', PetDetail.as_view(), name="pet"),
    path('adopt/<int:pet>/<int:logUser>/<int:owner>/', Adopt, name="adopt"),
    path('delete/<int:pet>/<int:cn>/', Delete, name="delete"),
    path('pets/', Pets, name="pets"),
]
