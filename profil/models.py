# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Profil(models.Model):
    user     = models.ForeignKey(User)
    civilite = models.CharField(max_length=3)
    adresse  = models.CharField(max_length=200)
    cp       = models.CharField(max_length=5)
    ville    = models.CharField(max_length=100)
    tel      = models.CharField(max_length=10)
    mobile   = models.CharField(max_length=10)
    siret    = models.IntegerField() # Pour Veto

    # La classe d un eventuel eleve peut etre gere grace au group django

    def __unicode__(self):
        return "%s %s" % (self.nom, self.prenom)


class Periode(models.Model):
    debut   = models.DateField()
    fin     = models.DateField()
    license = models.CharField(max_length = 60)
    profil  = models.ForeignKey(Profil)
