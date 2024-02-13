from django.shortcuts import render
import requests
from .models import Post

def home(request):
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    for post in response:
        Post.objects.create(title=post['title'], body=post['body'], price=5000)
        
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    
    return render(request, 'index.html', context)