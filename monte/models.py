#  -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from profil.models import Profil
from cheval.models import Cheval


class PeriodeMontoir(models.Model):
    chevaux_disponible = models.ManyToManyField(Cheval)


class CreneauMontoir(models.Model): # Fiche Vide
    semaine   = models.ForeignKey(PeriodeMontoir)
    date      = models.DateTimeField() # Pour gérer la date ET les heures
    classe    = models.CharField(max_length=65)
    remarque  = models.TextField()
    encadrant = models.ForeignKey(Profil)
    effectif  = models.CharField(max_length=65)
    duree     = models.FloatField()


class PiquetMontoirStaff(models.Model):
    montoir = models.ForeignKey(CreneauMontoir)
    cheval  = models.ForeignKey(Cheval) #parmis les chevaux_disponible de MontoirSemaine


class PiquetMontoirEnseignant(models.Model):
    montoir = models.ForeignKey(CreneauMontoir)
    cheval  = models.ForeignKey(Cheval) #parmis les chevaux_disponible de MontoirSemaine
    date    = models.DateField()
    profil  = models.ForeignKey(Profil) #cavalier
