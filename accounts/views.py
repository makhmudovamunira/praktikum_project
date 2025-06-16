from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data()
            user = authenticate(request,
                                username=data['username'],
                                password=data['password'])

            if user is not None:
                if user.is_active():
                    login(request, user)
                    return HttpResponse('Muvaffaqiyatli login amalga oshirildi!')
                else:
                    return HttpResponse('Sizning profilingiz activ emas')
            else:
                return HttpResponse('Login yoki parol xato')
    else:
        form = LoginForm()
        context={
            'form':form
        }
        return render(request, 'account/login.html', context)