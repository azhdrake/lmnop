from django.test import TestCase

from django.contrib.auth.models import User
from django.db import IntegrityError
# Create your tests here.


class TestUser(TestCase):

    def test_create_user_duplicate_username_fails(self):

        user = User(username='bob', email='bob@bob.com', first_name='bob', last_name='bob')
        user.save()

        user2 = User(username='bob', email='another_bob@bob.com', first_name='bob', last_name='bob')
        with self.assertRaises(IntegrityError):
            user2.save()


    def test_create_user_duplicate_username_case_insensitive_fails(self):

        user = User(username='bob', email='bob@bob.com', first_name='bob', last_name='bob')
        user.save()

        user2 = User(username='Bob', email='another_bob@bob.com', first_name='bob', last_name='bob')
        with self.assertRaises(IntegrityError):
            user2.save()


    def test_create_user_duplicate_email_fails(self):
        user = User(username='bob', email='bob@bob.com', first_name='bob', last_name='bob')
        user.save()

        user2 = User(username='bob', email='bob@bob.com', first_name='bob', last_name='bob')
        with self.assertRaises(IntegrityError):
            user2.save()


    def test_create_user_duplicate_email_case_insensitive_fails(self):
        user = User(username='bob', email='bob@bob.com', first_name='bob', last_name='bob')
        user.save()

        user2 = User(username='another_bob', email='Bob@bob.com', first_name='bob', last_name='bob')
        with self.assertRaises(IntegrityError):
            user2.save()

'''
    Show Table Test
'''
class TestShow(self):
    def test_add_show_successfully(self):
        artist = Artist(name='The Beatles')
        artist.save()
        venue = Venue(name='First Ave', city='Minneapolis', state='MN')
        venue.save()
        show = Show(artist=0, venue=0, name='Yellow Submarine', url='https://www.first-ave.com/shows/the-beatles-dec-31st/', time='8:30', ages='18', show_date='12/31/19')
        show.save()

    def test_duplicate_show(self):

        artist = Artist(name='The Beatles')
        artist.save()
        venue = Venue(name='First Ave', city='Minneapolis', state='MN')
        venue.save()
        show = Show(artist=0, venue=0, name='Yellow Submarine', url='https://www.first-ave.com/shows/the-beatles-dec-31st/', time='8:30', ages='18', show_date='12/31/19')
        show.save()

        show2 = Show(artist=0, venue=0, name='Yellow Submarine', url='https://www.first-ave.com/shows/the-beatles-dec-31st/', time='8:30', ages='18', show_date='12/31/19')
        with self.assertRaises(IntegrityError):
            show2.save()




