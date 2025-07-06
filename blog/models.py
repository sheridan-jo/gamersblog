from django.db import models
from django.conf import settings

#  Create your models here.
class Post(models.Model):
    """
    Represents a blog post
    """
    #  Creates a new field on Post to indicate if article is a draft or published
    DRAFT = 'draft'
    PUBLISHED = 'published'
    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')
    ]

    #  The post's title
    title = models.CharField(max_length=255, null=False, blank=False)

    #  The article's content
    content = models.TextField(null=True, blank=True)

    #  User that creates blog posts
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='blog_posts',
        null=False,
        blank=False,
    )

    #  Timestamp automatically set when created
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    #  Timestamp updated each time the object is saved
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    #  Create status of a post, published or draft
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=DRAFT,
        help_text='Set to "published" to make this post publicly visible',
        null=False,
        blank=False,
    )

    #  Timestamp to show when draft became published
    published = models.DateTimeField(
        null=True,
        blank=True,
        help_text='The date & time this article was published',
    )

    #  Creates a slug, a label used to form a URL path readable by humans
    slug = models.SlugField(
        null=False,
        blank=False,
        help_text='URL-friendly version of the title',
        unique_for_date='published',  # Slug is unique for publication date
    )

    topics = models.ManyToManyField('Topic', blank=True)

    #  Sets default ordering for Post objects
    class Meta:
        ordering = ['-created']  # Posts sorted by date created, newest first

    #  Post's title appears in list view rather than auto-generated string
    def __str__(self):
        return self.title

class Topic(models.Model):
    """
    Represents a topic
    """

    #  Topic's name
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        unique=True,
    )

    slug = models.SlugField(
        null=False,
        blank=False,
        unique=True,
        help_text='A URL-safe version of the topic name',
    )

    #  Topic's name rather than auto-generated string displayed
    def __str__(self):
        return self.name

class Comment(models.Model):
    """
    Represents a comment on a Post
    """

    #  Relationship to Post model
    post = models.ForeignKey(
        Post,
        related_name='comments',
        on_delete=models.CASCADE,  #  Comments deleted along with Post
        null=False,
        blank=False,
    )

    #  Name of the person commenting
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )

    #  Commenter's email address
    email = models.EmailField(null=False,blank=False)

    #  Field for the actual comment
    text = models.TextField(
        null=False,
        blank=False,
        max_length=255,
    )

    #  For comment moderation
    approved = models.BooleanField(default=False, blank=True)

    #  Timestamp automatically set when created
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    #  Timestamp updated each time the object is saved
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    #  Sets default ordering for Comments
    class Meta:
        ordering = ['-created']  # Comments sorted by date created, newest first

    #  Comment displayed rather than auto-generated string
    def __str__(self):
        return self.text[:30]  #  Returns first 30 characters
