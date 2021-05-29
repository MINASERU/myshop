from django.core.mail import send_mail
from django.conf import settings
def send_code(message, email):
    return send_mail('blog', message, settings.EMAIL_FROM,[email,])