# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# from django.contrib.auth.models import User, Group


categorie_choices = (
    ('1','Elève'),
    ('2','Cavalier'),
    ('3','Professeur'),
    ('4','Personnel'),
    ('5','Autre'), #veto ?
    )


civilite_choices = (
    ('1','Mr'),
    ('2','Mme'),
    ('3','Mlle'),
    )

class Profil(models.Model):
    civilite   = models.CharField(max_length=3,
                                choices = civilite_choices)
    nom        = models.CharField(max_length=200)
    prenom     = models.CharField(max_length=200)
    email      = models.CharField(max_length=200)
    adresse    = models.CharField(max_length=200)
    cp         = models.CharField(max_length=5)
    ville      = models.CharField(max_length=100)
    tel_1      = models.CharField(max_length=10)
    tel_2      = models.CharField(max_length=10)
    tel_3      = models.CharField(max_length=10)
    # categorie  = models.CharField(max_length=100, choices=categorie_choices)


    def __unicode__(self):
        return "%s %s" % (self.nom, self.prenom)


class Public(models.Model):
    nom = models.CharField(max_length=30)

    def __unicode__(self):
        return "%s" % (self.nom)


class Periode(models.Model):
    debut   = models.DateField()
    fin     = models.DateField(null=True, blank=True)
    license = models.CharField(max_length = 60)
    public  = models.ForeignKey(Public)
    profil  = models.ForeignKey(Profil)

    def __unicode__(self):
        return "%s %s %s" % (self.debut, self.fin, self.license)
