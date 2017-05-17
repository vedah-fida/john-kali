from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core import urlresolvers

# Create your views here.

def index(request):
    return render(request, 'myapp/index.html', locals())
def second_view(request):
    return render(request, 'myapp/second_page.html', locals())

def user_login(request):
    postdata = request.POST.copy()
    username = postdata.get('username', '')
    password = postdata.get('password', '')
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        login(request, user)
        url = urlresolvers.reverse('index:basic_view')
        return HttpResponseRedirect(url)
    else:
        error_msg = "Check your password and username again"
        return render(request, 'myapp/second_page.html', locals())

def logout_user(request):
    logout(request)
    url = urlresolvers.reverse('index:index')
    return HttpResponseRedirect(url)































