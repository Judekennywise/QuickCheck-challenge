from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Comment, PollOption, AllStories, Story, Poll, Job


def add_obj_id(sender, instance, created, **kwargs):
    if created and not instance.obj_id:
        instance.obj_id = instance.id
        instance.save()


@receiver(post_save, sender=Comment)
def comment(sender, instance, created, **kwargs):
    add_obj_id(sender, instance, created, **kwargs)


@receiver(post_save, sender=PollOption)
def poll_option(sender, instance, created, **kwargs):
    add_obj_id(sender, instance, created, **kwargs)

@receiver(post_save, sender=AllStories)
def all(sender, instance, created, **kwargs):
    add_obj_id(sender, instance, created, **kwargs)
@receiver(post_save, sender=Story)
def story(sender, instance, created, **kwargs):
    add_obj_id(sender, instance, created, **kwargs)
@receiver(post_save, sender=Job)
def poll(sender, instance, created, **kwargs):
    add_obj_id(sender, instance, created, **kwargs)
@receiver(post_save, sender=Poll)
def job(sender, instance, created, **kwargs):
    add_obj_id(sender, instance, created, **kwargs)