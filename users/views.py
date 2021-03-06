from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
# from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == "POST":

        form = UserRegisterForm(request.POST)
        # print(form)
        # print(form.is_valid())
        # print(form.errors)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # messages.debug
            # messages.info
            # messages.success
            # messages.warning
            # messages.error
            messages.success(request, f'Your account has been created. You are now able to login')
            return HttpResponseRedirect(reverse('login'))
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form":form})



@login_required
def profile(request):

    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance = request.user) #pass instance of current user
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile) #get the images in request.FILES
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return HttpResponseRedirect(reverse('profile'))

    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, "users/profile.html", context)

















#
