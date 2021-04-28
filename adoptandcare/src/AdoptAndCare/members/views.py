from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from .forms import *
from .models import *
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class LoginView(LoginRequiredMixin):
    login_url = 'registration/login/'
    redirect_field_name = "decide"

    def get(self, request):
        return self.render_to_response({})


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')



class CreateProfileView(generic.CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = "registration/profile.html"
    success_url = reverse_lazy('home')
    

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    
    def get_context_data(self, *args, **kwargs):
        context = super(CreateProfileView, self).get_context_data(*args, **kwargs)
        context['mes'] = "Create your profile"
        return context


def decide(req):
    profile_exist = Profile.objects.filter(user=req.user)
    if(profile_exist):
        # return redirect('edit_profile', req.user.pk)
        return redirect('pets')
    else:
        return redirect('create_profile')


class UserPage(DetailView):
    model = User
    template_name = "registration/user_page.html"

    def get_context_data(self, *args, **kwargs):
        context = super(UserPage, self).get_context_data(*args, **kwargs)
        active_user = get_object_or_404(User, id=self.kwargs['pk'])
        este = Profile.objects.filter(user=active_user)
        pets = Pet.objects.filter(user=active_user)
        context["active_user"] = active_user
        context["pets"] = pets
        context["cat_is"] = pets.count()
        context["este"] = este
        return context


class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'registration/editprofile.html'
    success_url = reverse_lazy('home')

    
    def get_context_data(self, *args, **kwargs):
        context = super(ProfileEditView, self).get_context_data(*args, **kwargs)
        context['mes'] = "Edit your profile"
        print(self.kwargs['pk'])
        pr = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['pr'] = pr
        context['settings'] = False
        print(pr)
        return context
        

class UserEditView(UpdateView):
    model = User
    form_class = EditUserView
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        context = super(UserEditView, self).get_context_data(*args, **kwargs)
        pr = get_object_or_404(User, id=self.kwargs['pk'])
        print(pr)
        context['pr'] = pr
        context['settings'] = True
        return context


 
