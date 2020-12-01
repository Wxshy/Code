from django.shortcuts import render
from .models import Post

posts = [
    {
        'author':'Sam W',
        'title':'First Post',
        'content':'This is the content of the post',
        'date_posted':'30/11/2020'
    },
    {
        'author':'James L',
        'title':'Productive CS Lesson',
        'content':'OMG I PACKED KANE',
        'date_posted':'30/11/2020'
    }
]

def home(request):
    context = {
            'posts':Post.objects.all()
        }
    
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
