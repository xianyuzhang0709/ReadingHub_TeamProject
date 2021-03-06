from django.http import HttpResponse, HttpResponse
from readinghub.models import Category, Book, Event, UserProfile
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserForm, UserProfileForm, BookForm, BookForm_withoutCat
from django.contrib.auth.decorators import login_required
# from django.core.urlresolvers import reverse
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import User


def index(request):
    context_dict = {}
    category_list = Category.objects.all()
    book_list = Book.objects.order_by('-likes')[:6]
    context_dict['categories'] = category_list
    context_dict['books'] = book_list
    response = render(request, 'readinghub/index.html', context_dict)
    return response


def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        books = Book.objects.filter(category=category).order_by('-likes')
        context_dict['books'] = books
        context_dict['category'] = category
        context_dict['category_name_slug'] = category_name_slug

    except Category.DoesNotExist:
        context_dict['books'] = None
        context_dict['category'] = None
        context_dict['category_name_slug'] = None

    return render(request, 'readinghub/category.html', context_dict)


def show_book(request, category_name_slug, book_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        book = Book.objects.get(slug=book_name_slug)
        context_dict['book'] = book
        context_dict['category'] = category
        context_dict['category_name_slug'] = category_name_slug
        context_dict['book_name_slug'] = book_name_slug
    except Category.DoesNotExist or Book.DoesNotExist:
        context_dict['category'] = None
        context_dict['book'] = None
        context_dict['category_name_slug'] = None
        context_dict['book_name_slug'] = None

    return render(request, 'readinghub/show_book.html', context_dict)


def show_event(request, event_name_slug):
    context_dict = {}

    try:
        events = Event.objects.get(slug=event_name_slug)
        context_dict['events'] = events
        context_dict['event_name_slug'] = event_name_slug
    except Event.DoesNotExist:
        context_dict['event'] = None
        context_dict['event_name_slug'] = None

    return render(request, 'readinghub/show_event.html', context_dict)



def recommend_book(request, category_name_slug, username):
    try:
        category = Category.objects.get(slug=category_name_slug)
        recommender = User.objects.get(username=username)
    except Category.DoesNotExist:
        category = None
        recommender = None
    form = BookForm_withoutCat()
    if request.method == 'POST':
        form = BookForm_withoutCat(request.POST)
        if form.is_valid():
            if category:
                newbook = form.save(commit=False)
                newbook.category = category
                newbook.recommender = recommender
                if 'image' in request.FILES:
                    newbook.image = request.FILES['image']
                newbook.save()
            return show_category(request, category_name_slug)
        else:
            print(form.errors)

    context_dict = {'form': form, 'category': category}
    return render(request, 'readinghub/recommend_book.html', context_dict)


def recommend_a_book(request, username):
    try:
        recommender = User.objects.get(username=username)
    except:
        recommender = None
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            newbook = form.save(commit=False)
            newbook.recommender = recommender
            category_name_slug = newbook.category.slug
            if 'image' in request.FILES:
                newbook.image = request.FILES['image']
            newbook.save()
            return show_category(request, category_name_slug)
        else:
            print(form.errors)

    context_dict = {'form': form}
    return render(request, 'readinghub/recommend_a_book.html', context_dict)


# Book list for Book.html
def all_book(request):
    book_list = Book.objects.order_by('-likes')
    context_dict = {'books': book_list}
    response = render(request, 'readinghub/book.html', context_dict)
    return response


def about(request):
    response = render(request, 'readinghub/about.html')
    return response

# like button
@login_required
def like_book(request):
    bookid = None
    if request.method == 'GET':
        bookid = request.GET['book_id']
        if bookid:
            boook = Book.objects.get(id=int(bookid))
            if boook:
                likes = boook.likes + 1
                boook.likes = likes
                boook.save()
    return HttpResponse(likes)

# join button
@login_required
def join_event(request):
    eventid = None
    if request.method == 'GET':
        eventid = request.GET['event_id']
        participators = 0
        if eventid:
            evvent = Event.objects.get(id=int(eventid))
            if evvent:
                participators = evvent.participators + 1
                evvent.participators = participators
                evvent.save()
    return HttpResponse(participators)


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
                   'registered': registered,})


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
        return render(request, 'readinghub/login.html',)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

# after first time registered, heading to create profile for the user
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

# show profile page for every user
def profile(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('index')
    userprofile = UserProfile.objects.get_or_create(user=user)[0]
    try:
        userbooks = Book.objects.filter(recommender=user)
    except Book.DoesNotExist:
        userbooks = None

    form = UserProfileForm(
        {'picture': userprofile.picture, 'description': userprofile.description})
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        if form.is_valid():
            form.save(commit=True)
            return redirect('profile', user.username)
        else:
            print(form.errors)
    return render(request, 'readinghub/profile.html', {'userprofile': userprofile,
                                                       'selecteduser': user, 'form': form, 'userbooks': userbooks})

# Best Reader
def list_profiles(request):
    userprofile_list = UserProfile.objects.all()
    return render(request, 'readinghub/list_profiles.html', {'userprofile_list': userprofile_list})

# event list for event.html
def event(request):
    event_order_list = Event.objects.order_by('-participators')
    context_dict = {'events': event_order_list}
    response = render(request, 'readinghub/event.html', context_dict)
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
