from django.urls import path
from .views import *

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("create_profile/", CreateProfileView.as_view(), name="create_profile"),
    path("decide/", decide, name="decide"),
    path("login/", LoginView , name="login"),
    path('<int:pk>/edit_profile/', ProfileEditView.as_view(), name="edit_profile"),
    path('<int:pk>/edit_settings/', UserEditView.as_view(), name="edit_settings"),
    path("<int:pk>/users/", UserPage.as_view(), name="active_user"),
]
