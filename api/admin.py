from django.contrib import admin

# Register your models here.
from api.models import Post, Comment, Category , CustomUser

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(CustomUser)
admin.site.register(Category)
