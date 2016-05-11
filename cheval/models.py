# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext as _
from datetime import date


STATUS_CHOICES = (
    ("1", "Propriété"),
    ("2", "Commodat"),
    ("3", "Pension"),
    ("4", "Débourrage"),
    ("5", "Divers"),
)

ACTIVITE_CHOICES = (
    ("1", "Monte"),
    ("2", "Elevage"),
)

APTITUDE_CHOICES = (
    ("1", "Apte"),
    ("2", "Repos"),
    ("3", "Infirmerie"),
    ("4", "Autres"),
)


class Emplacement(models.Model):
    zone = models.CharField(max_length = 200)
    box  = models.CharField(max_length = 200, unique = True, null = True)

    def __unicode__(self):
        return "Zone %s - box %s" % (self.zone, self.box)


class Cheval(models.Model):
    sire            = models.IntegerField(unique = True)
    nom             = models.CharField(max_length = 200)
    race            = models.CharField(max_length = 100)
    pedigree        = models.CharField(max_length = 500)
    annee_naissance = models.CharField(max_length = 60)
    photo           = models.CharField(max_length = 500)
    date_entree     = models.DateField(default = date.today())
    date_sortie     = models.DateField(null=True)
    activite        = models.CharField(max_length = 1, choices = ACTIVITE_CHOICES)
    remarques       = models.TextField()
    status          = models.CharField(max_length = 1, choices = STATUS_CHOICES)
    aptitude        = models.CharField(max_length = 1, choices = APTITUDE_CHOICES, default = "1")
    emplacement     = models.OneToOneField( Emplacement,
                                            unique = True,
                                            verbose_name = _('emplacement'),
                                            related_name = 'emplacement')

    def __unicode__(self):
        return "%s %s %s" % (self.nom, self.sire, self.emplacement)
