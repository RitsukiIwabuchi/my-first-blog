import datetime

from django.test import TestCase, Client
from django.utils import timezone
from django.urls import reverse

from .models import Post

def create_blog(title, text):
    return Post.objects.create(title=title, text=text)
