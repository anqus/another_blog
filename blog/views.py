from django.shortcuts import render

posts = [
    {
        'author': 'Angus',
        'title': 'Blog Post 1',
        'content': 'Post 1 Content',
        'date_posted': '26/07/2020',
    },
    {
        'author': 'Angus',
        'title': 'Blog Post 2',
        'content': 'Post 2 Content',
        'date_posted': '27/07/2020',
    },
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})