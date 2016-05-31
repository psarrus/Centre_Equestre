# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import date


STATUS_CHOICES = (
    ("1", "Propriété"),
    ("2", "Commodat"),
    ("3", "Pension"),
    ("4", "Débourrage"),
    ("5", "Autres"),
)

ACTIVITE_CHOICES = (
    ("1", "Monte"),
    ("2", "Élevage"),
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
    photo           = models.FileField(upload_to = "photos")
    date_entree     = models.DateField(auto_now_add = True)
    date_sortie     = models.DateField(null = True, blank = True)
    activite        = models.CharField(max_length = 1, choices = ACTIVITE_CHOICES)
    remarques       = models.TextField()
    statut          = models.CharField(max_length = 1, choices = STATUS_CHOICES)
    aptitude        = models.CharField(max_length = 1, choices = APTITUDE_CHOICES, default = "1")
    emplacement     = models.OneToOneField(Emplacement, unique = True)

    class Meta:
        verbose_name_plural = "Chevaux"

    def get_dernier_soin(self):
        return self.registresoins_set.filter(acte=1).order_by("-date").first()

    def get_dernier_vaccin(self):
        return self.registresoins_set.filter(acte=2).order_by("-date").first()

    def get_dernier_ferrage(self):
        return self.registresoins_set.filter(acte=3).order_by("-date").first()

    def get_derniere_vermifugation(self):
        return self.registresoins_set.filter(acte=4).order_by("-date").first()

    def __unicode__(self):
        return self.nom
