from django.test import TestCase
from datetime import datetime
from contact.models import Contact

class ContactModelTest(TestCase):
    def setUp(self):
        self.obj = Contact(
            name='Guilherme Cortez',
            phone='53-12345-6789',
            email='gui200cortez@gmail.com',
            message='Esta é uma mensagem de teste.'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Contact.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.obj.recieved_at, datetime)

    def test_str(self):
        self.assertEqual(str(self.obj), 'Guilherme Cortez')

    def test_anwsered_default_False(self):
        self.assertEqual(False, self.obj.anwsered)

    def test_phone_optional(self):
        obj_without_phone = Contact(
            name='Guilherme Cortez',
            email='gui200cortez@gmail.com',
            message='Mensagem sem telefone'
        )
        obj_without_phone.save()
        self.assertTrue(Contact.objects.filter(name='Guilherme Cortez').exists())
