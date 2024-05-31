from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string, get_template
from django.utils.html import strip_tags
from django.conf import settings

from django.core.mail import EmailMessage
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template import Context
from django.template.loader import get_template


# Create your views here.

def testemail(request):
    context = {
        "receiver_name": "Saium Khan",
        "age": 27,
        "profession": "Software Developer",
        "marital_status": "Divorced",
        "address": "Planet Earth",
        "year": 2023
    }
    message = get_template("default.html").render(context)
    mail = EmailMessage(
        subject="Order confirmation",
        body=message,
        from_email='test@myemail.com',
        to=['send@toemail.com'],
        reply_to=['test@myemail.com'],
    )
    mail.content_subtype = "html"
    mail.send()

    #
    # receiver_email = "saium@abcinc.com"
    # template_name = "default.html"
    # convert_to_html_content = render_to_string(
    #     template_name=template_name,
    #     context=context
    # )
    # plain_message = strip_tags(convert_to_html_content)
    #
    # mail_sent = send_mail(
    #     subject="Receiver information from a form",
    #     message=plain_message,
    #     from_email=settings.EMAIL_HOST_USER,
    #     recipient_list=[receiver_email, ],
    #     html_message=convert_to_html_content,
    #     fail_silently=True
    # )
    return HttpResponse("Email sent")