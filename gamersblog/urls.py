"""
URL configuration for Gamers' Blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from blog import views  #  Import the blog views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),  #  Set root to home view
    path('about/', views.AboutView.as_view(), name='about'),
    path('terms/', views.terms_and_conditions, name='terms-and-conditions'),
    path('topics/', views.TopicListView.as_view(), name='topic-list'),  # For Topic ListView
    path('topics/<slug:slug>/', views.TopicDetailView.as_view(), name='topic-detail'), # Topic DetailView
    path("posts/<slug:slug>/", views.PostDetailView.as_view(), name='post-detail'),  # Post DetailView
    path("posts/", views.PostListView.as_view(), name='post-list'),  #  Post ListView
    path('contact/', views.ContactFormView.as_view(), name='contact'),  # Contact form
    path('contest/', views.PhotoSubmission.as_view(), name='photo-contest')  #  Photo contest
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
