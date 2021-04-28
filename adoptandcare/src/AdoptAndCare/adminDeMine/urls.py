from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/',  admin, name="admin"),
    path('deleteUser/<int:pk>',  deleteUser, name="deleteUser"),
    path('deleteEmail/<int:pk>',  deleteEmail, name="deleteEmail"),
    path('deleteAdoptedPet/<int:pk>/<int:pet>',  deleteAdoptedPet, name="deleteAdoptedPet"),
]