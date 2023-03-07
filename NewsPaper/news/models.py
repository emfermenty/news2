from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


# Create your models here.

class Author(models.Model):
    auth_rating = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def update_rating(self):
        pass


class Category(models.Model):
    category_name = models.CharField(max_length=255, unique = True)

    def __str__(self):
        return f'{self.category_name}'

article = 'ART'
news = 'NEW'
CHOICES = [(article, 'Статья'),
        (news, 'Новость')]


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_time = models.DateTimeField(auto_now_add = True)
    post_type = models.CharField(max_length=3, choices = CHOICES, default = news)
    title = models.CharField(max_length=255)
    content = models.TextField()
    post_rating = models.IntegerField(default=0)
    category = models.ManyToManyField(Category, through = 'PostCategory')

    def preview(self):
        return self.content[:124] + '...'

    def like(self):
        self.post_rating += 1
        self.save()

    def dislike(self):
        self.post_rating -= 1
        self.save()

    def __str__(self):
        return f'{self.category} : {self.author} : {self.title}: {self.content}: rating = {self.post_rating}'

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)



    pass

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=300)
    comment_time = models.DateTimeField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0)

    def like(self):
        self.comment_rating += 1
        self.save()

    def dislike(self):
        self.comment_rating -= 1
        self.save()

    def __str__(self):
        return f'{self.comment_text}: {self.comment_time} {self.comment_rating}'