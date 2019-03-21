from django.http import HttpResponse, HttpResponse
from readinghub.models import Category, Book, Event, UserProfile
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserForm, UserProfileForm, BookForm
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from datetime import datetime
from django.contrib.auth.models import User


def index(request):
    event_list = Event.objects.all()
    event1 = event_list[0]
    event2 = event_list[1]
    event3 = event_list[2]
    category_list = Category.objects.all()
    book_list = Book.objects.order_by('-likes')[:3]
    context_dict = {'categories': category_list, 'books': book_list, 'event1': event1, 'event2': event2,
                    'event3': event3}
    response = render(request, 'readinghub/index.html', context_dict)
    return response


def show_category(request, category_name_slug):
    event_list = Event.objects.all()
    event1 = event_list[0]
    event2 = event_list[1]
    event3 = event_list[2]
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        books = Book.objects.filter(category=category).order_by('-likes')
        context_dict['books'] = books
        context_dict['category'] = category
        context_dict['category_name_slug'] = category_name_slug
        context_dict['event_list'] = event_list
        context_dict['event1'] = event1
        context_dict['event2'] = event2
        context_dict['event3'] = event3

    except Category.DoesNotExist:
        context_dict['books'] = None
        context_dict['category'] = None
        context_dict['category_name_slug'] = None

    return render(request, 'readinghub/category.html', context_dict)


def show_book(request, category_name_slug, book_name_slug):
    event_list = Event.objects.all()
    event1 = event_list[0]
    event2 = event_list[1]
    event3 = event_list[2]
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        book = Book.objects.get(slug=book_name_slug)
        context_dict['book'] = book
        context_dict['category'] = category
        context_dict['category_name_slug'] = category_name_slug
        context_dict['book_name_slug'] = book_name_slug
        context_dict['event1'] = event1
        context_dict['event2'] = event2
        context_dict['event3'] = event3
    except Category.DoesNotExist or Book.DoesNotExist:
        context_dict['category'] = None
        context_dict['book'] = None
        context_dict['category_name_slug'] = None
        context_dict['book_name_slug'] = None

    return render(request, 'readinghub/show_book.html', context_dict)


def show_event(request, event_name_slug):
    event_list = Event.objects.all()
    event1 = event_list[0]
    event2 = event_list[1]
    event3 = event_list[2]
    context_dict = {}

    try:
        events = Event.objects.get(slug=event_name_slug)
        context_dict['events'] = events
        context_dict['event_name_slug'] = event_name_slug
        context_dict['event1'] = event1
        context_dict['event2'] = event2
        context_dict['event3'] = event3
    except Event.DoesNotExist:
        print("0000000")
        context_dict['event'] = None
        context_dict['event_name_slug'] = None

    return render(request, 'readinghub/show_event.html', context_dict)



def recommend_book(request, category_name_slug):
    event_list = Event.objects.all()
    event1 = event_list[0]
    event2 = event_list[1]
    event3 = event_list[2]
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        
    except Category.DoesNotExist:
        category = None

    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            if category:
                newbook = form.save(commit=False)
                newbook.category = category
                if 'image' in request.FILES:
                    newbook.image = request.FILES['image']

                newbook.save()
            return show_category(request, category_name_slug)
        else:
            print(form.errors)

    context_dict = {'form': form, 'category': category,'event1': event1, 'event2': event2,'event3': event3}
    return render(request, 'readinghub/recommend_book.html', context_dict)


def all_book(request):
    event_list = Event.objects.all()
    event1 = event_list[0]
    event2 = event_list[1]
    event3 = event_list[2]
    context_dict = {}
    book_list = Book.objects.order_by('-likes')
    context_dict = {'books': book_list,'event1': event1, 'event2': event2,'event3': event3}
    response = render(request, 'readinghub/book.html', context_dict)
    return response


def about(request):
    event_list = Event.objects.all()
    event1 = event_list[0]
    event2 = event_list[1]
    event3 = event_list[2]
    context_dict = {}
    context_dict['event1'] = event1
    context_dict['event2'] = event2
    context_dict['event3'] = event3
    response = render(request, 'readinghub/about.html',context_dict)
    return response


def show_each_book(request):
    event_list = Event.objects.all()
    event1 = event_list[0]
    event2 = event_list[1]
    event3 = event_list[2]
    context_dict = {}
    context_dict['event1'] = event1
    context_dict['event2'] = event2
    context_dict['event3'] = event3
    response = render(request, 'readinghub/show_each_book.html',context_dict)
    return response


@login_required
def like_book(request):
    bookid = None
    if request.method == 'GET':
        bookid = request.GET['book_id']
        likes = 0
        if bookid:
            boook = Book.objects.get(id=int(bookid))
            if boook:
                likes = boook.likes + 1
                boook.likes = likes
                boook.save()
    return HttpResponse(likes)

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
    event_list = Event.objects.all()
    event1 = event_list[0]
    event2 = event_list[1]
    event3 = event_list[2]
    context_dict = {}
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
    context_dict = {'form': form,'event1': event1, 'event2': event2,'event3': event3}
    return render(request, 'readinghub/profile_registration.html', context_dict)


@login_required
def profile(request, username):
    event_list = Event.objects.all()
    event1 = event_list[0]
    event2 = event_list[1]
    event3 = event_list[2]
    context_dict = {}
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
    return render(request, 'readinghub/profile.html', {'userprofile': userprofile, 'selecteduser': user, 'form': form,'event1': event1, 'event2': event2,'event3': event3})


@login_required
def list_profiles(request):
    event_list = Event.objects.all()
    event1 = event_list[0]
    event2 = event_list[1]
    event3 = event_list[2]
    context_dict = {}
    userprofile_list = UserProfile.objects.all()
    return render(request, 'readinghub/list_profiles.html', {'userprofile_list': userprofile_list,'event1': event1, 'event2': event2,'event3': event3})


def event(request):
    # Queries the database of a list of all books currently stored.
    # Order the books by number of likes in descending order
    event_list = Event.objects.all()
    event1 = event_list[0]
    event2 = event_list[1]
    event3 = event_list[2]
    context_dict = {}
    event_list = Event.objects.all()
    context_dict = {'events': event_list,'event1': event1, 'event2': event2,'event3': event3}
    response = render(request, 'readinghub/event.html', context_dict)
    return response


def book(request):
    # Queries the database of a list of all books currently stored.
    # Order the books by number of likes in descending order
    event_list = Event.objects.all()
    event1 = event_list[0]
    event2 = event_list[1]
    event3 = event_list[2]
    context_dict = {}
    book_list = Book.objects.order_by('-likes')[:5]
    context_dict = {'books': book_list,'event1': event1, 'event2': event2,'event3': event3}
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
