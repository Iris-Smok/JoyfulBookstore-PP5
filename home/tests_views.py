""" test views for home and contact page"""
from django.test import TestCase


class TestView(TestCase):
    """ Test for views home and contact page page"""

    def test_get_home_page(self):
        """ test to check that home page is diplayed"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_get_contact_page(self):
        """ test to check that home page is diplayed"""
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/contact.html')
