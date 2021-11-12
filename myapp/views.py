from django.shortcuts import redirect, render

from .models import Posts

def home_page(request):
    all_posts = Posts.objects.all()[:10]   #ogranicili smo postove na 10 da ne izlistava 100 komada na naslovnoj strani
    list_all_posts = {'all_posts' : all_posts}
    return render(request, 'home_page.html', list_all_posts)


def details(request, id):
    one_result = Posts.objects.get(id=id)
    one_post = {"one_result" : one_result}
    return render(request, 'details.html', one_post)


def admin(request):
    response = redirect('admin')
    return response