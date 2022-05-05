from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from .models import Order,Delivery
from django.conf import settings

@receiver(post_save,sender=Order)
def send_notification_about_order(instance, created,**kwargs):
    if created:
        send_mail(subject="new message",message="Your order created.",from_email=settings.DEFAULT_FROM_EMAIL,recipient_list=[instance.user.email])

# @receiver(post_save,sender=Delivery)
# def send_notification_about_order(instance, created,**kwargs):
#     if instance.canceled:
#         template = f"Delivery {instance.id} canceled"
#         send_mail(subject=template,recipient
# 
# _list=[instance.user.email])


#         @receiver(post_save,sender=Delivery)


# def send_notification_about_order(instance, created,**kwargs):
#     if instance.canceled:
#         template = f"Delivery {instance.id} canceled"
#         send_mail(subject=template,recipient_list=[instance.user.email])

@receiver(post_save,sender=Order)
def send_notification_about_order(instance, created,**kwargs):
    if instance.canceled:
        # ////
        template = f"Order {instance.id} canceled"
        send_mail(subject="new message",message=template,from_email=settings.DEFAULT_FROM_EMAIL,recipient_list=[instance.user.email])


@receiver(post_save,sender=Delivery)
def send_notification_about_order(instance, created,**kwargs):
    if created:
        send_mail(subject="new message",message="Your Delivery created.",from_email=settings.DEFAULT_FROM_EMAIL,recipient_list=[instance.user.email])



@receiver(post_save,sender=Delivery)
def send_notification_about_order(instance, created,**kwargs):
    if instance.canceled:
        template = f"Delivery {instance.id} canceled"
        send_mail(subject="new message",message=template,from_email=settings.DEFAULT_FROM_EMAIL,recipient_list=[instance.user.email])