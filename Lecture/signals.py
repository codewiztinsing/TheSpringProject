from .models import Lecture
from django.dispatch import receiver
from django.db.models.signals import post_save

@receiver(post_save,sender = Lecture)
def post_save_create_profile(sender,instance,created,*args,**kwargs):
	if created:
		Lecture.objects.create(user = instance)