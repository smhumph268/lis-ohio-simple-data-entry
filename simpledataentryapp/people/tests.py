from django.test import TestCase
from django.urls import reverse


"""
TODO: add more tests (e.g. add test for navigating to a confirmation page that doesn't exist, confirmation page tests,
more happy path, edge cases, etc.)
"""


class AddNewUserTests(TestCase):

    def setUp(self):
        self.newPersonURL = reverse('people:new')

    def test_viewing_form(self):
        response = self.client.get(
            self.newPersonURL,
            follow=True
        )
        self.assertTrue(response.content.decode(response.charset).__contains__('Add A New Person'))
        self.assertTrue(response.content.decode(response.charset).__contains__('Name:'))
        self.assertTrue(response.content.decode(response.charset).__contains__('Title:'))
        self.assertTrue(response.content.decode(response.charset).__contains__('Hometown:'))

    def test_only_required_fields(self):
        response = self.client.post(
            self.newPersonURL,
            {
                'name': 'Shane',
                'title': 'The Applier',
                'age': '',
                'hometown': ''
            },
            follow=True
        )
        self.assertTrue(response.content.decode(response.charset).__contains__(
            'New row for \'Shane\' with title: \'The Applier\''))

    def test_missing_name(self):
        response = self.client.post(
            self.newPersonURL,
            {
                'name': '',
                'title': 'The Applier',
                'age': '',
                'hometown': ''
            },
            follow=True
        )
        self.assertTrue(response.content.decode(response.charset).__contains__('This field is required'))

    def test_missing_title(self):
        response = self.client.post(
            self.newPersonURL,
            {
                'name': 'Shane',
                'title': '',
                'age': '',
                'hometown': ''
            },
            follow=True
        )
        self.assertTrue(response.content.decode(response.charset).__contains__('This field is required'))

    def test_age_below_min(self):
        response = self.client.post(
            self.newPersonURL,
            {
                'name': 'Shane',
                'title': 'The Applier',
                'age': '-1',
                'hometown': ''
            },
            follow=True
        )
        self.assertTrue(response.content.decode(response.charset).__contains__('error-text'))

    def test_age_above_max(self):
        response = self.client.post(
            self.newPersonURL,
            {
                'name': 'Shane',
                'title': 'The Applier',
                'age': '124',
                'hometown': ''
            },
            follow=True
        )
        self.assertTrue(response.content.decode(response.charset).__contains__('error-text'))
