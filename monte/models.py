#  -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.db.models import Q
from django.db.models.signals import  post_save
from django.dispatch import receiver

from profil.models import Profil, Public
from cheval.models import Cheval

import datetime

jour_choices = (
    ('1','lundi'),
    ('2','mardi'),
    ('3','mercredi'),
    ('4','jeudi'),
    ('5','vendredi'),
    )

class CreneauMontoir(models.Model):
    jour        = models.CharField(max_length=1,
                            choices = jour_choices)
    heure_debut = models.TimeField()
    duree       = models.FloatField()
    effectif    = models.CharField(max_length=65)
    encadrant   = models.ForeignKey(Profil)
    remarque    = models.TextField(blank=True)
    public      = models.ForeignKey(Public)

class CreneauMontoirEnseignant(models.Model):
    date            = models.DateField(null=True, blank=True)
    creneau_montoir = models.ForeignKey(CreneauMontoir, null=True)


class PiquetMontoirStaff(models.Model):
    montoir  = models.ForeignKey(CreneauMontoir, related_name='piquet_staff')
    cheval   = models.ForeignKey(Cheval)
    selected = models.BooleanField(default=False)

    def serialize(self):
        return {
            'montoir': self.montoir,
            'cheval': self.cheval,
            'selected': self.selected,
            }

class PiquetMontoirEnseignant(models.Model):
    montoir  = models.ForeignKey(CreneauMontoir, null=True, related_name='piquet_enseignant')
    date     = models.DateField(null=True, blank=True)
    cheval   = models.ForeignKey(Cheval)
    selected = models.BooleanField(default=False)
    profil   = models.ForeignKey(Profil, null=True)
    # piquet_montoir_staff = models.ForeignKey(PiquetMontoirStaff, null=True, related_name='piquet_enseignant')






@receiver(post_save, sender=CreneauMontoir)

def create_piquet_montoir_staff(sender, instance, created, **kwargs):
    if created:
        for cheval in Cheval.objects.filter(Q(date_sortie__gte=datetime.date.today()) | Q(date_sortie__isnull=True),activite="1"):

            PiquetMontoirStaff.objects.create(montoir=instance,
                                              cheval=cheval)

            # PiquetMontoirEnseignant.objects.create(montoir=instance,
            #                                        cheval=cheval)



# @receiver(post_save, sender=PiquetMontoirStaff)
#
# def update_piquet_montoir_enseignant(sender, instance, update_fields, **kwargs):
#     print "OK"
#     PiquetMontoirEnseignant.objects.create(montoir=instance,
#                                             cheval=instance)
