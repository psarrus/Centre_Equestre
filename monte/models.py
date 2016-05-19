#  -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from profil.models import Profil, Public
from cheval.models import Cheval

jour_choices = (
    ('1','lundi'),
    ('2','mardi'),
    ('3','mercredi'),
    ('4','jeudi'),
    ('5','vendredi'),
    )

class CreneauMontoir(models.Model): # Fiche Vide
    jour = models.CharField(max_length=1,
                            choices = jour_choices)
    heure_debut = models.TimeField()
    duree     = models.FloatField()
    effectif  = models.CharField(max_length=65)
    encadrant = models.ForeignKey(Profil)
    remarque  = models.TextField(blank=True)
    public    = models.ForeignKey(Public)

class PiquetMontoirStaff(models.Model):
    montoir = models.ForeignKey(CreneauMontoir)
    cheval  = models.ManyToManyField(Cheval) #parmis les chevaux_disponible de MontoirSemaine


class PiquetMontoirEnseignant(models.Model):
    montoir = models.ForeignKey(CreneauMontoir)
    cheval  = models.ForeignKey(Cheval) #parmis les chevaux_disponible de MontoirSemaine
    date    = models.DateField()
    profil  = models.ForeignKey(Profil) #cavalier
