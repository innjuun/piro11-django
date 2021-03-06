from django.db import models
from django.forms import ValidationError
from django.conf import settings
import re

from django.shortcuts import resolve_url
from django.urls import reverse


def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name





class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    title = models.CharField(max_length=100,
                             verbose_name="제목",
                             help_text='포스팅 제목을 입력해주세요',
                             )
    content = models.TextField(verbose_name="내용")
    photo = models.ImageField(blank=True, upload_to='blog/post/%Y/%m/%d')
    tags = models.CharField(max_length=100, blank=True, )
    lnglat = models.CharField(max_length=50, validators=[lnglat_validator],
                              help_text='경도,위도 포맷으로 입력', blank=True, )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    tag_set = models.ManyToManyField('Tag', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.id])
# class User(models.Model):
#     idd = models.CharField(max_length=20)
#     password = models.CharField(max_length=20)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
