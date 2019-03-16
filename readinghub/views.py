from django.http import HttpResponse
from readinghub.models import Category, Book, Event
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm


def index(request):
    response = render(request, 'readinghub/index.html')
    return response


def about(request):
    response = render(request, 'readinghub/about.html')
    return response


def register(request):
    response = render(request, 'readinghub/register.html')
    return response


def login(request):
    response = render(request, 'readinghub/login.html')
    return response


def logout(request):
    return 0


def event(request):
    response = render(request, 'readinghub/event.html')
    return response


def book(request):
    response = render(request, 'readinghub/book.html')
    return response


class UserFormView(View):
    form_class = UserForm
    template_name = ''

    # displays a blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # processes form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # cleaned data (formats data so it enters database properly)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns user objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:

                    login(request, user)
                    return redirect('index')

            return render(request, self.template_name, {'forms': form})
