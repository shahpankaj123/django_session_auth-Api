from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

def send_activation_email(recipient_email, activation_url):
    subject = 'Activate your account on '
    from_email = settings.EMAIL_HOST_USER
    to = [recipient_email]

    html_content = render_to_string('account/activation_email.html', {'activation_url': activation_url,'topic':'Activation Mail','desc':'Youre receiving this email because you need to finish activation process.'})
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(subject, text_content, from_email, to)
    email.attach_alternative(html_content, "text/html")
    email.send()

def send_reset_password_email(recipient_email, activation_url):
    subject = 'Reset Password'
    from_email = settings.EMAIL_HOST_USER
    to = [recipient_email]

    html_content = render_to_string('account/activation_email.html', {'activation_url': activation_url,'topic':'Reset Password Mail','desc':'Youre receiving this email because you need to Reset Password process.'})
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(subject, text_content, from_email, to)
    email.attach_alternative(html_content, "text/html")
    email.send()    