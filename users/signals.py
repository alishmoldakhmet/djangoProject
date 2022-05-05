from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import User
from django.core.mail import send_mail
from django.conf import settings


@receiver(post_save,sender=User)
def send_welcome_mail(instance,created,**kwargs):
    if created:
        res = send_mail(subject="New message",message="YOU HAVE REGISTERED",from_email=settings.DEFAULT_FROM_EMAIL,recipient_list=[instance.email])