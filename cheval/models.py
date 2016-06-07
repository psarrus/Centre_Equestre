# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date


STATUT_CHOICES = (
    ('1', 'Propriété'),
    ('2', 'Commodat'),
    ('3', 'Pension'),
    ('4', 'Débourrage'),
    ('5', 'Autres'),
)

ACTIVITE_CHOICES = (
    ('1', 'Monte'),
    ('2', 'Élevage'),
)

APTITUDE_CHOICES = (
    ('1', 'Apte'),
    ('2', 'Repos'),
    ('3', 'Infirmerie'),
    ('4', 'Autres'),
)


class Emplacement(models.Model):
    zone    = models.CharField(max_length = 100)
    box     = models.CharField(max_length = 100, unique = True, null = True)

    def __unicode__(self):
        return 'Zone %s - box %s' % (self.zone, self.box)


class Cheval(models.Model):
    sire            = models.IntegerField(unique = True)
    nom             = models.CharField(max_length = 100)
    race            = models.CharField(max_length = 100)
    pedigree        = models.CharField(max_length = 100)
    annee_naissance = models.IntegerField()
    photo           = models.FileField(upload_to = 'photos')
    date_entree     = models.DateField(auto_now_add = True)
    date_sortie     = models.DateField(null = True, blank = True)
    activite        = models.CharField(max_length = 1, choices = ACTIVITE_CHOICES)
    remarques       = models.TextField()
    statut          = models.CharField(max_length = 1, choices = STATUT_CHOICES)
    aptitude        = models.CharField(max_length = 1, choices = APTITUDE_CHOICES, default = '1')
    emplacement     = models.OneToOneField(Emplacement, unique = True)

    class Meta:
        verbose_name_plural = 'Chevaux'

    def get_dernier_soin(self):
        return self.soin_set.filter(acte = 1).order_by('-date').first()

    def get_dernier_vaccin(self):
        return self.soin_set.filter(acte = 2).order_by('-date').first()

    def get_dernier_ferrage(self):
        return self.soin_set.filter(acte = 3).order_by('-date').first()

    def get_derniere_vermifugation(self):
        return self.soin_set.filter(acte = 4).order_by('-date').first()

    def __unicode__(self):
        return self.nom


@receiver(post_save, sender = Cheval)

def add_cheval_piquet_montoir_staff(sender, instance, created, **kwargs):
    from monte.models import CreneauMontoir, PiquetMontoirStaff
    if created:
        for montoir in CreneauMontoir.objects.all():
            PiquetMontoirStaff.objects.create(montoir = montoir, cheval = instance)


@receiver(post_save, sender = Cheval)

def del_cheval_piquet_montoir_staff(sender, instance, update_fields, created, **kwargs):
    from monte.models import CreneauMontoir, PiquetMontoirStaff
    if created == False and instance.date_sortie <= date.today():
        for montoir in CreneauMontoir.objects.all():
            PiquetMontoirStaff.objects.filter(cheval = instance).delete()




        # for cheval in Cheval.objects.filter(Q(date_sortie__gte=datetime.date.today()) | Q(date_sortie__isnull=True),activite="1"):
        #
        #     PiquetMontoirStaff.objects.create(montoir=instance,
        #                                 cheval=cheval)
        #
        #
        # user = User(   email=instance.email,
        #                first_name=instance.prenom,
        #                last_name=instance.nom,
        #                username=instance.nom,
        #                is_active=instance.profil_actif)
        # user.set_password("plop48000")
        # user.save()
        # instance.user = user
        # instance.save()
