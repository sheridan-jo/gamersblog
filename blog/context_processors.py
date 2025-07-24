from django.db.models import Count

#  Returns the 10 topics with the most posts
def base_context(request):
    from . import models

    #  Counts number of posts for topics and returns the 10 with the most posts
    topics_list = (
        models.Topic.objects
        .annotate(post_count=Count('post', distinct=True))
        .order_by('-post_count')[:10]
    )

    return {'topics_list': topics_list}
