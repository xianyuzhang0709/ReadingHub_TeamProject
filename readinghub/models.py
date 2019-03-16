from django.contrib import admin
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    url = models.URLField()
    description = models.TextField(blank=True)
    likes = models.IntegerField(default=0)

    # reviews = models.ForeignKey(Reviews)

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=128, unique=True)
    venue = models.CharField(max_length=128)
    date = models.DateField()
    time = models.TimeField()
    book = models.ForeignKey("Book", blank=True, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey("UserProfile", blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User Model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    picture = models.ImageField(upload_to='profile_images', blank=True)
    description = models.TextField(blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __str__(self):
        return self.user.username


