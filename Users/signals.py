from django.db.models.signals import post_save

'''The import User is known as the Sender '''
from django.contrib.auth.models import User
from django.dispatch import receiver
from IT6041App.models import Customer


@receiver(post_save, sender=User)
def create_customer(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance, name=instance.username, email=instance.email)


@receiver(post_save, sender=User)
def save_customer(sender, instance, **kwargs):
    instance.customer.save()


