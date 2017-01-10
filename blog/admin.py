from django.contrib import admin
from .models import Post
from .models import Comment

admin.site.register(Post)
admin.site.register(Comment)
## To make our model visible on the admin page we need to register it with admin