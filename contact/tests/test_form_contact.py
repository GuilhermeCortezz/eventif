from django.test import TestCase
from contact.forms import ContactForm

class ContactFormTest(TestCase):
    def setUp(self):
        self.form = ContactForm()

    def test_has_form(self):
        expected = ['name', 'phone', 'email', 'message']
        self.assertSequenceEqual(expected, list(self.form.fields))