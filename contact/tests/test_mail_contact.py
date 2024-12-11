from django.test import TestCase
from django.core import mail
from django.shortcuts import resolve_url as r

class ContactPostValid(TestCase):
    def setUp(self):
        data = dict(name="Guilherme Cortez", phone="", email="gui200cortez@gmail.com", message="Mensagem de teste para contato!")
        self.client.post(r('contact:new'), data)
        self.email = mail.outbox[0]

    def test_contact_email_subject(self):
        expect = 'Confirmação de contato!'
        self.assertEqual(expect, self.email.subject)
    
    def test_contact_email_from(self):
        expect = 'gui200cortez@gmail.com'
        self.assertEqual(expect, self.email.from_email)

    def test_contact_email_to(self):
        expect = ['gui200cortez@gmail.com', 'contato@eventif.com.br']
        self.assertEqual(expect, self.email.to)

    def test_contact_email_body(self):
        contents = (
            ('Guilherme Cortez'),
            (''),
            ('gui200cortez@gmail.com'),
            ('Mensagem de teste para contato!')
        )
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)