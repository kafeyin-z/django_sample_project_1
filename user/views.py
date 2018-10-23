from django.shortcuts import render, HttpResponseRedirect, reverse
from user.forms import girisForm, kayitForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.


def giris(request):
    form = girisForm(data=request.POST or None)
    context = {'form': form}
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('blog-listele'))
        else:
            msg = "Böyle bir kullanıcı yok"
            context = {'form': form, 'msg': msg}
    return render(request, 'user/giris.html', context=context)


def cikis(request):
    logout(request)
    return HttpResponseRedirect(reverse('blog-listele'))


def kayit(request):
    form = kayitForm(data=request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        newuser = User(username=username)
        newuser.set_password(password)
        newuser.save()

        login(request, newuser)

        return HttpResponseRedirect(reverse('blog-listele'))
    context = {
        "form": form
    }
    return render(request, 'user/kayit.html', context=context)
