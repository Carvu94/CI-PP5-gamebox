from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .forms import ContactForm


def contact(request):

    """ View function for the contact us form """

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            ticket = form.save()
            messages.info(request, 'Message sent!')

            """Send the user a confirmation email"""
            user_email = ticket.email
            name = form.cleaned_data['name']
            user_message = form.cleaned_data['message']
            subject = form.cleaned_data['inquiry_purpose']
            message = render_to_string(
                'confirmation_email/confirmation_email.txt', {
                    'name': name,
                    'message': user_message
                })

            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [user_email]
            )

            return redirect(reverse('contact'))
        else:
            messages.error(request, 'Failed to send message. \
            Try again.')
    else:
        form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
