# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver



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
    user       = models.OneToOneField(User, null=True)
    civilite   = models.CharField(max_length=3, choices = civilite_choices)
    nom        = models.CharField(max_length=200)
    prenom     = models.CharField(max_length=200)
    email      = models.CharField(max_length=200)
    adresse    = models.CharField(max_length=200)
    cp         = models.CharField(max_length=5)
    ville      = models.CharField(max_length=100)
    tel_1      = models.CharField(max_length=10)
    tel_2      = models.CharField(max_length=10)
    tel_3      = models.CharField(max_length=10)


    def __unicode__(self):
        return "%s %s" % (self.nom, self.prenom)


class Public(models.Model):
    nom = models.CharField(max_length=30)

    def __unicode__(self):
        return "%s" % (self.nom)


class Periode(models.Model):
    categorie  = models.CharField(max_length=100, choices=categorie_choices)
    public     = models.ForeignKey(Public, null=True, blank=True)
    license    = models.CharField(max_length = 60, null=True, blank=True)
    debut      = models.DateField()
    fin        = models.DateField(null=True, blank=True)
    profil     = models.ForeignKey(Profil)

    def __unicode__(self):
        return "%s %s %s" % (self.debut, self.fin, self.license)



@receiver(post_save, sender=Profil)
def create_user(sender, created, instance, **kwargs):
    if created:
        user = User.objects.create(email=instance.email,
                                   first_name=instance.prenom,
                                   last_name=instance.nom,
                                   username=instance.email,
                                   password='plop',
                                   is_active=False)
        instance.user = user
        instance.save()
