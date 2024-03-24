from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
# from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key
from users.models import Users




# @cache_page(30) # Guarda a página toda em cache
def users(request):


    users = Users.objects.all().order_by('name')


    context = {
        'users' : users,
        'x' : timezone.now,
    }
    return render(request, 'users.html', context)



def cache_clear_users(request):

    cache.delete(make_template_fragment_key('users'))

    return redirect('users')



def cache_clear(request):

    cache.clear()

    return redirect('users')