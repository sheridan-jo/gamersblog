from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from . import models

#  Home view
class HomeView(TemplateView):
    template_name = 'blog/home.html'

    #  Returns the 3 most recent posts in order of date published
    def get_context_data(self, **kwargs):
        #  Get parent context
        context = super().get_context_data(**kwargs)

        #  Selects 3 most recent published posts
        latest_posts = models.Post.objects.filter(status='published') \
                           .order_by('-published')[:3]
        #  Adds latest_posts to context variable
        context.update({'latest_posts': latest_posts})
        return context

#  About view
class AboutView(TemplateView):
    template_name = 'blog/about.html'

# Topic ListView
class TopicListView(ListView):
    model = models.Topic
    context_object_name = 'topics'
    ordering = 'name'

# DetailView for topic
class TopicDetailView(DetailView):
    model = models.Topic

    def get_context_data(self, **kwargs):
        #  Overrides get_context_data(), so context variables can be customized
        context_data = super().get_context_data(**kwargs)
        topic = self.get_object()  #  Allows access to topic object

        #  Returns published posts that match the topic, ordered by most recent
        posts = (models.Post.objects.filter(topics=topic, status='published')
                 .order_by('-published'))
        context_data['posts'] = posts  #  Adds posts to context_data dictionary
        return context_data

# ListView for posts
class PostListView(ListView):
    model = models.Post
    context_object_name = 'posts'

    #  Returns published posts in order of date published
    def get_queryset(self):
        queryset = (super().get_queryset().filter(status='published')
                    .order_by('-published'))
        return queryset

# DetailView for post
class PostDetailView(DetailView):
    model = models.Post

    #  Returns published post
    def get_queryset(self):
        queryset = super().get_queryset().filter(status='published')
        return queryset

#  Terms and conditions view
def terms_and_conditions(request):
    return render(request, 'blog/terms_and_conditions.html')
