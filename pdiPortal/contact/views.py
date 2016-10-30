from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

from .forms import contactForm

# Create your views here.
def contact(request):
    title = 'Contact PDi-PORTAL Admin'
    form = contactForm(request.POST or None)
    confirm_message = None

    if form.is_valid():
        comment = form.cleaned_data['comment']
        name = form.cleaned_data['name']
        subject = 'Message from PDi-PORTAL'
        message = '%s\n\n%s' %(comment, name)
        email_from = form.cleaned_data['email']
        email_to = [settings.DEFAULT_FROM_EMAIL]
        send_mail(subject, message, email_from, email_to, fail_silently = False)
        title = "Thanks"
        confirm_message = "Thanks for the message! We will get back to you as soon as possible."
        form = None

    context = {'title': title, 'form': form, 'confirm_message': confirm_message}

    template = 'contact.html'
    return render(request, template, context)