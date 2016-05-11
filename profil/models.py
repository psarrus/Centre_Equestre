# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# from django.contrib.auth.models import User


categorie_choices = (
    ('1','Elève'),
    ('2','Cavalier'),
    ('3','Professeur'),
    ('4','Personnel'),
    ('5','Autre'), #veto ?
    )

class Profil(models.Model):
    # user   = models.ForeignKey(User)
    nom        = models.CharField(max_length=200) # A spprimer si User
    prenom     = models.CharField(max_length=200) # A spprimer si User
    email      = models.CharField(max_length=200) # A spprimer si User
    civilite   = models.CharField(max_length=3)
    adresse    = models.CharField(max_length=200)
    cp         = models.CharField(max_length=5)
    ville      = models.CharField(max_length=100)
    tel        = models.CharField(max_length=10)
    mobile     = models.CharField(max_length=10)
    categorie  = models.CharField(max_length=1,
                                choices = categorie_choices)
    siret    = models.IntegerField(null=True) # Pour Veto

    # La classe d un eventuel eleve peut etre gere grace au group django

    def __unicode__(self):
        return "%s %s" % (self.nom, self.prenom)


class Periode(models.Model):
    debut   = models.DateField()
    fin     = models.DateField()
    license = models.CharField(max_length = 60)
    profil  = models.ForeignKey(Profil)
