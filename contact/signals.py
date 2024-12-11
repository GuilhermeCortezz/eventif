from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from contact.models import Contact

@receiver(post_save, sender=Contact)
def send_response_email(sender, instance, created, **kwargs):
    if not created and instance.anwsered and instance.anwser:
        send_mail(
            f"Resposta ao seu contato - {instance.name}",
            instance.anwser,
            settings.DEFAULT_FROM_EMAIL,
            [instance.email, settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )
