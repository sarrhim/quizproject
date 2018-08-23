from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from authentification.forms import SignUpForm
from quiz.models import studentClass


@login_required

def home(request):
    return render(request, 'registration/home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            st = invitation.all().filter(student=request.user.email)
            if st != null:
                for k in st:
                    sc = studentClass()
                    sc.professor = k.prof
                    sc.student = request.user
                    sc.exam = k.exams
                    sc.email_invited = k.student
                    sc.save()
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
