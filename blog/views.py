from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

# display the blog
def post_detail(request, pk):
    post = get_object_or_404(Post,  pk=pk)
    return render(request, 'blog/post_detail.html',  {'post': post})
