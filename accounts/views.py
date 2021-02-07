from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile


# Create your views here.

@login_required
def dashboard(request):
    profile = Profile.objects.get_or_create(user=request.user)[0]
    return render(request, 'account/dashboard.html', {'section': 'dashboard', 'profile': profile})


# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'], password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse('Authenticated ''successfully')
#                 else:
#                     return HttpResponse('Disabled account')
#             else:
#                 return HttpResponse('Invalid login')
#     else:
#         form = LoginForm()
#     return render(request, 'account/login.html', {'form': form})
#
#
# def register(request):
#     if request.method == 'POST':
#         user_form = UserRegistrationForm(request.POST)
#         if user_form.is_valid():
#             # create a new user object but avoid saving it yet
#             new_user = user_form.save(commit=False)
#             # set the chosen password
#             new_user.set_password(
#                 user_form.cleaned_data['password']
#             )
#             # save the user object
#             new_user.save()
#             # create the user profile
#             Profile.objects.create(user=new_user)
#             context = {'new_user': new_user}
#             return render(request, 'account/register_done.html', context)
#     else:
#         user_form = UserRegistrationForm()
#     context = {'user_form': user_form}
#     return render(request, 'account/register.html', context)


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('dashboard')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'account/edit.html', context)


