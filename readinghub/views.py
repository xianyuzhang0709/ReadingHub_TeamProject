from django.http import HttpResponse, HttpResponse
from readinghub.models import Category, Book, Event, UserProfile
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from datetime import datetime
from django.contrib.auth.models import User


def index(request):
    response = render(request, 'readinghub/index.html')
    return response


def about(request):
    response = render(request, 'readinghub/about.html')
    return response


def register(request):
    registered = False
    if request.method == 'POST':
            user_form = UserForm(data=request.POST)
            profile_form = UserProfileForm(data=request.POST)

            if user_form.is_valid() and profile_form.is_valid():
                user = user_form.save()
                user.set_password(user.password)
                user.save()

                profile = profile_form.save(commit=False)
                profile.user = user

                if 'picture' in request.FILES:
                    profile.picture = request.FILES['picture']

                profile.save()
                registered = True

            else:
                print(user_form.errors, profile_form.errors)

    else:
            # These forms will be blank, ready for user input.
            user_form = UserForm()
            profile_form = UserProfileForm()

    return render(request, 'readinghub/register.html',
                       {'user_form': user_form,
                        'profile_form': profile_form,
                        'registered': registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'readinghub/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def register_profile(request):
    form = UserProfileForm()
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()

            return redirect('index')
        else:
            print(form.errors)
    context_dict = {'form': form}
    return render(request, 'readinghub/profile_registration.html', context_dict)


@login_required
def profile(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('index')
    userprofile = UserProfile.objects.get_or_create(user=user)[0]
    form = UserProfileForm(
        {'picture': userprofile.picture, 'description': userprofile.description})
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        if form.is_valid():
            form.save(commit=True)
            return redirect('profile', user.username)
        else:
            print(form.errors)
    return render(request, 'readinghub/profile.html', {'userprofile': userprofile, 'selecteduser': user, 'form': form})


@login_required
def list_profiles(request):
    userprofile_list = UserProfile.objects.all()
    return render(request, 'readinghub/list_profiles.html', {'userprofile_list' : userprofile_list})


def event(request):
    # Queries the database of a list of all books currently stored.
    # Order the books by number of likes in descending order

    event_list = Event.objects.all()
    context_dict = {'events': event_list}
    response = render(request, 'readinghub/event.html', context_dict)
    return response


def book(request):
    # Queries the database of a list of all books currently stored.
    # Order the books by number of likes in descending order

    book_list = Book.objects.order_by('-likes')[:5]
    context_dict = {'books': book_list}
    response = render(request, 'readinghub/book.html', context_dict)
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
