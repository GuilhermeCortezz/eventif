# Generated by Django 5.1 on 2024-12-11 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nome')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='telefone')),
                ('email', models.EmailField(max_length=254, verbose_name='e-mail')),
                ('message', models.CharField(max_length=500, verbose_name='mensagem')),
                ('recieved_at', models.DateTimeField(auto_now_add=True, verbose_name='recebido em')),
                ('anwser', models.CharField(blank=True, max_length=500, verbose_name='resposta')),
                ('anwsered_at', models.DateTimeField(blank=True, null=True, verbose_name='respondido em')),
                ('anwsered', models.BooleanField(default=False, verbose_name='respondido')),
            ],
            options={
                'verbose_name': 'contato',
                'verbose_name_plural': 'contatos',
                'ordering': ('-recieved_at',),
            },
        ),
    ]
