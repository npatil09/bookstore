from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm

@login_required
def edit_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile')  # Redirect to view profile page
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'userprofile/profile.html', {'form': form})

@login_required
def view_profile(request):
    profile = request.user.profile
    return render(request, 'userprofile/view_profile.html', {'profile': profile})
