# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


STATUS_CHOICES = (
    (1, "Propriété"),
    (2, "Commodat"),
    (3, "Pension"),
    (4, "Débourrage"),
    (5, "Divers"),
)

EMPLACEMENT_CHOICES = (
    (1, "Emplacement 1"),
    (2, "Emplacement 2"),
    (3, "Emplacement 3"),
    (4, "Emplacement 4"),
    (5, "Emplacement 5"),
)

ACTIVITE_CHOICES = (
    (1, "Monte"),
    (2, "Elevage"),
)


class Aptitude(models.Model): #ex: apte repos infiremerie ...
    aptitude = models.CharField(max_length=100, default="apte")


class Status(models.Model):
    status = models.CharField(max_length = 500, choices=STATUS_CHOICES)
    divers = models.TextField()


class Emplacement(models.Model):
    emplacement = models.CharField(max_length = 500, choices=EMPLACEMENT_CHOICES)
    remarque    = models.TextField() # Etat de l'enclo


class Cheval(models.Model):
    sire            = models.IntegerField(unique=True)
    nom             = models.CharField(max_length = 200)
    race            = models.CharField(max_length = 100)
    pedigree        = models.CharField(max_length = 500)
    annee_naissance = models.CharField(max_length = 60)
    photo           = models.CharField(max_length = 500)
    date_entree     = models.DateField()
    date_sortie     = models.DateField()
    activite        = models.CharField(max_length = 500, choices=ACTIVITE_CHOICES)
    remarques       = models.CharField(max_length = 60)
    status          = models.ForeignKey(Status)
    emplacement     = models.ForeignKey(Emplacement)
    aptitude        = models.ForeignKey(Aptitude)

    def __unicode__(self):
        return "%s %s" % (self.nom, self.sire)
