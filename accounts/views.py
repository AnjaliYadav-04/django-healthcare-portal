from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import SignupForm

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignupForm()
    return render(request, "signup.html", {"form": form})

@login_required
def dashboard_view(request):
    if request.user.user_type == 'doctor':
        return render(request, "doctor_dashboard.html", {"user": request.user})
    else:
        return render(request, "patient_dashboard.html", {"user": request.user})
