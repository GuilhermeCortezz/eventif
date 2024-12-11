from django.db import models

class Contact(models.Model):
    name = models.CharField('nome', max_length=100)
    phone = models.CharField('telefone', max_length=20, blank=True, null=True)
    email = models.EmailField('e-mail')
    message = models.CharField('mensagem', max_length=500)
    recieved_at = models.DateTimeField('recebido em', auto_now_add=True)
    anwser = models.TextField('resposta', max_length=500, null=True, blank=True)
    anwsered_at = models.DateTimeField('respondido em', null=True, blank=True)
    anwsered = models.BooleanField('respondido', default=False)

    class Meta:
        verbose_name_plural = 'contatos'
        verbose_name = 'contato'
        ordering = ('-recieved_at',)

    def __str__(self):
        return self.name
