from django.test import TestCase
from readinghub.models import Category, Event, Book
from django.core.urlresolvers import reverse

class IndexViewTests(TestCase):

    def test_index_view_with_no_categories(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no categories present.")
        self.assertQuerysetEqual(response.context['categories'], [])


class BookMethodTests(TestCase):

    def test_slug_creation(self):
        cat = Category(name='test')
        cat.save()
        book = Book(title='random book string', category=cat, author='test',
                    url='http://testtesttest.com')
        book.save()
        self.assertEqual(book.slug, 'random-book-string')


    def test_book_page_show_all_books(self):
        cat0 = Category(name='test_b')
        cat0.save()
        recommend_book(cat0, 'test1', 'author1', 'http://test1.com', 'd1', )
        recommend_book(cat0, 'test2', 'author2', 'http://test2.com', 'd2', )
        recommend_book(cat0, 'test3', 'author3', 'http://test3.com', 'd3', )
        response = self.client.get(reverse('book'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test3")
        num_bs = len(response.context['books'])
        self.assertEqual(num_bs, 3)



def recommend_book(category, title, author, url, description):
    b = Book.objects.create(category=category, title=title, author=author, likes=0,
                            url=url, description=description)
    b.save()
    return b
