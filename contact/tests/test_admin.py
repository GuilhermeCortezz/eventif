from django.test import TestCase
from contact.admin import ContactModelAdmin, Contact, admin
from unittest.mock import Mock

class ContactModelAdminTest(TestCase):
    def setUp(self):
        Contact.objects.create(name="Guilherme Cortez", phone='53-91234-56789', email='gui200cortez@gmail.com', message='Mensagem de teste')
        self.model_admin = ContactModelAdmin(Contact, admin.site)

    def test_has_action(self):
        self.assertIn('mark_as_answered', self.model_admin.actions)

    def test_mark_all(self):
        mock = self.call_action()
        self.assertEqual(1, Contact.objects.filter(anwsered=True).count())

    def test_message(self):
        mock = self.call_action()
        mock.assert_called_once_with(None, '1 contato(s) foi(ram) marcado(s) como respondido(s).')

    def call_action(self):
        queryset = Contact.objects.all()

        mock = Mock()
        old_message_user = ContactModelAdmin.message_user
        ContactModelAdmin.message_user = mock

        self.model_admin.mark_as_answered(None, queryset)

        ContactModelAdmin.message_user = old_message_user

        return mock
