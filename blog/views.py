from django.shortcuts import render
from . import models
from django.db.models import Count

# Create your views here.

def home(request):
    """
    The Gamers' Blog Homepage
    """

    #  Render the list of topics contained in Topic model
    topics_list = (
        models.Topic.objects
        .annotate(post_count=Count('post', distinct=True))  # Counts posts for Topics
        .order_by('-post_count')[:10]  #  Limits to top 10 posts
    )

    #  Add as context variable "topics_list"
    context = {'topics_list': topics_list}

    return render(request, 'blog/home.html', context)
