from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Profil)
def create_user(sender, created, instance, **kwargs):
    if created:
        user = User.objects.create(email=instance.email,
                                   first_name=instance.prenom,
                                   last_name=instance.nom,
                                   username=instance.email,
                                   password='plop',
                                   is_active=False)
        instance.user = user
        instance.save()
