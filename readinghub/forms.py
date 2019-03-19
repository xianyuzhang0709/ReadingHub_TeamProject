from django.contrib.auth.models import User
from django import forms
from readinghub.models import Book, Category, UserProfile

class BookForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the book.")
    author = forms.CharField(max_length=128, help_text="Please enter the author's name of the book.")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the book.")
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    description = forms.CharField(widget=forms.Textarea, help_text="Please description this book.")
    image = forms.ImageField(required=False, help_text="Upload a picture of the book.")

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

            return cleaned_data

    class Meta:
        model = Book
        exclude = ('category',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('picture', 'description')
