from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class MasterProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user", verbose_name="User")
    profession = models.CharField(max_length=100, verbose_name="Profession")
    avatar = models.ImageField(upload_to="masters/", blank=True, null=True, verbose_name="profile photo")


    class Meta:
        verbose_name_plural = "Masters"

    def __str__(self):
        return f'{self.user.first_name}-{self.user.last_name}'
    
    @receiver(post_save, sender=User)
    def create_user_info(sender, instance, created, **kwargs):
        if created and instance.is_staff:
            master = MasterProfile(user=instance)
            master.save()