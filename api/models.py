from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from api.managers import CustomUserManager


class CustomUser(AbstractUser):
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = CustomUserManager()


class Staff(CustomUser):
    class Meta:
        proxy = True


class Visitor(CustomUser):
    class Meta:
        proxy = True


class Post(models.Model):
    class Meta:
        ordering = ('created',)

    title = models.CharField(max_length=100, default='')
    body = models.TextField(blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('CustomUser', related_name='posts', on_delete=models.CASCADE)


class Comment(models.Model):
    class Meta:
        ordering = ('created',)

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('CustomUser', related_name='comments', on_delete=models.CASCADE)


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'categories'

    name = models.CharField(max_length=100, blank=False)
    owner = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='categories')
    posts = models.ManyToManyField(Post, related_name='categories', blank=True)
