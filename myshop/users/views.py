from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from .models import Profile
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("myapp:index")
    form = NewUserForm()
    context = {'form': form}
    return render(request, 'register.html', context)

def custom_logout(request):
    if request.method == 'POST':
        logout(request)
        return render(request, 'logout.html')
    return render(request, 'logout.html')


@login_required
def profile(request):
    if request.method == "POST":
        contact_number = request.POST.get("number")
        image = request.FILES["upload"]
        user = request.user
        profile = Profile(user=user, contact_number=contact_number, image=image)
        profile.save()
    return render(request, 'profile.html')

def seller_profile(request, id):
    seller = User.objects.get(id=id)

    context = {'seller': seller}
    return render(request, 'sellerprofile.html', context)
