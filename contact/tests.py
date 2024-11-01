from django.test import TestCase
from django.core import mail
from contact.forms import ContactForm

class ContactTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/contato/')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'contact/contact_form.html')

    def test_html(self):
        self.assertContains(self.response, '<form')
        self.assertContains(self.response, '<input', 5)
        self.assertContains(self.response, 'type="text"', 2)
        self.assertContains(self.response, '<textarea', 1)
        self.assertContains(self.response, 'type="email"')
        self.assertContains(self.response, 'type="submit"')

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        form = self.response.context['form']
        self.assertSequenceEqual(['name', 'phone', 'email', 'message'], list(form.fields))

class ContactPostTest(TestCase):
    def setUp(self):
        data = dict(name="Guilherme Cortez", phone="", email="gui200cortez@gmail.com", message="Mensagem de teste para contato!")
        self.resp = self.client.post('/contato/', data)

    def test_post(self):
        self.assertEqual(302, self.resp.status_code)

    def test_send_subscription_email(self):
        self.assertEqual(1, len(mail.outbox))

    def test_subscription_email_subject(self):
        email = mail.outbox[0]
        expect = 'Confirmação de contato!'
        self.assertEqual(expect, email.subject)
    
    def test_subscription_email_from(self):
        email = mail.outbox[0]
        expect = 'gui200cortez@gmail.com'
        self.assertEqual(expect, email.from_email)

    def test_subscription_email_to(self):
        email = mail.outbox[0]
        expect = ['contato@eventif.com.br', 'gui200cortez@gmail.com']
        self.assertEqual(expect, email.to)

    def test_subscription_email_body(self):
        email = mail.outbox[0]
        self.assertIn('Guilherme Cortez', email.body)
        self.assertIn('', email.body)
        self.assertIn('gui200cortez@gmail.com', email.body)
        self.assertIn('Mensagem de teste para contato!', email.body)

class ContactInvalidPost(TestCase):
    def setUp(self):
        self.resp = self.client.post('/contato/', {})

    def test_post(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'contact/contact_form.html')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, ContactForm)
    
    def test_form_has_error(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)

class ContactSucessMessage(TestCase):
    def test_message(self):
        data = dict(name="Guilherme Cortez", phone="", email="gui200cortez@gmail.com", message="Mensagem de teste para contato!")
        resp = self.client.post('/contato/', data, follow=True)
        self.assertContains(resp, 'Mensagem enviada com sucesso!')