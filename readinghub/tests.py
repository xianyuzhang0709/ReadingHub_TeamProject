from django.test import TestCase
from readinghub.models import Book
from django.shortcuts import render
from django.views.generic.base import View
from custom_user.forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.test import Client

User = get_user_model()

# Create your tests here.

class LoginTests(TestCase):
    def test_user_log_in(self):
        user = User.objects.create(username='XixixiHaha')
        user.set_password('zxyzxy223')
        user.save()
        c = Client()
        login = c.login(username='XixixiHaha', password='zxyzxy223')
        self.assertTrue(login)

class ClassifyMethodTests(TestCase):
    def test_ensure_classify_are_not_empty(self):
        b = Book(name='AnythingYouWant')
        b.save()
        self.assertEqual((b.title != ''), True)

class IndexViewTests(TestCase):
    def test_index_view_when_not_login(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "login")
        self.assertContains(response, "register")




