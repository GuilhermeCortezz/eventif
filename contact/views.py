from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, resolve_url as r
from contact.forms import ContactForm
from contact.models import Contact
from django.core import mail
from django.template.loader import render_to_string
from django.contrib import messages
from django.conf import settings

def contact(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)

def create(request):
    form = ContactForm(request.POST)

    if not form.is_valid():
        return render(request, 'contact/contact_form.html', {'form': form})

    #salvar no banco
    contact = Contact.objects.create(**form.cleaned_data)

    #mail
    _send_mail('contact/contact_email.txt', {'contact': contact}, 'Confirmação de contato!', contact.email, settings.DEFAULT_FROM_EMAIL)

    return HttpResponseRedirect(r('contact:detail', contact.pk))

def new(request):
    return render(request, 'contact/contact_form.html', {'form': ContactForm()})

def detail(request, pk):
    try:
        contact = Contact.objects.get(pk=pk)
    except Contact.DoesNotExist:
        raise Http404
    return render(request, 'contact/contact_detail.html', {'contact': contact})

def _send_mail(template_name, context, subject, from_, to):
    body = render_to_string(template_name, context)
    email = mail.send_mail(subject, body, from_, [from_, to])