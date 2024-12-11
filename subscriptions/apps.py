from django.apps import AppConfig


class SubscriptionsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "subscriptions"
    verbose_name = "Controle de Participantes"

class ContactsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "contacts"
    verbose_name = "Controle de Contatos"
