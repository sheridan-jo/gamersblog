from django.contrib import admin
from . import models

#  Custom ModelAdmin for the Post model
class PostAdmin(admin.ModelAdmin):
    list_display = (  #  Fields to be displayed in the list view
        'title',
        'author',
        'status',
        'created',
        'updated',
    )

    search_fields = (  # Enables search feature
        'title',
        'author__username',
        'author__first_name',
        'author__last_name',
    )

    list_filter = ('status', 'topics')  #  Filters results by status and topics

    ordering = ['created']  # Posts sorted by date created, oldest first

    prepopulated_fields = {'slug': ('title',)}   # Automates generation of slugs

#  Custom ModelAdmin for the Topic model
class TopicAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']  #  Topic fields to be displayed

#  Register the models
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Topic, TopicAdmin)
