from django.shortcuts import render
from .forms import UserEditForm,ProfileEditForm
from accounts.forms import UserRegistrationForm
from .models import Profile

# Create your views here.
def dashboard_view(request):
    user = request.user
    profile_form = ProfileEditForm(instance=request.user_profile,
                                   data=request.POST,
                                   files=request.FILES)
    context = {
        "user":user,
        "profile_form": profile_form
    }
    return render(request,"pages/user_profile.html",context=context)

def user_register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        new_user = user_form.save(commit=False)
        new_user.set_password(
            user_form.cleaned_data["password"]
        )
        new_user.save()
        Profile.objects.crete(self=new_user)
        context = {
            "new_user":new_user
        }
        return render(request,"account/register_done.html",context)
    else:
        user_form = UserRegistrationForm()
        context = {
            "user_form":user_form
        }
        return render(request,"account/register.html",context)

def edit_user(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user,data=request.POST)
        profile_form = ProfileEditForm(instance=request.user_profile,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user)
    return render(request,"account/profile_edit.html",{"user_form":user_form,"profile_form":profile_form})
































