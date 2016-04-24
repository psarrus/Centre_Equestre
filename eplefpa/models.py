#  -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Profil(models.Model):
    civilite = models.CharField(max_length=3)
    nom = models.CharField(max_length = 60)
    prenom = models.CharField(max_length = 60)
    adresse = models.CharField(max_length=200)
    cp = models.CharField(max_length=5)
    ville = models.CharField(max_length=100)
    tel = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10)
    mail = models.CharField(max_length=300)

    def __unicode__(self):
        return "%s %s" % (self.nom, self.prenom)

class Cavalier(models.Model):
    profil = models.ForeignKey(Profil)
    licence = models.IntegerField()
    date_debut = models.DateField()
    date_fin = models.DateField()

class Encadrant(models.Model):
    profil = models.ForeignKey(Profil)
    date_debut = models.DateField()
    date_fin = models.DateField()

class Discipline(models.Model): #ex: trot cross galop dressage ...
    discipline = models.CharField(max_length=100)

    def __unicode__(self):
        return "%s" % technique

class Aptitude(models.Model): #ex: apte repos infiremerie ...
    aptitude = models.CharField(max_length=100)

    def __unicode__(self):
        return "%s" % aptitude

class Cheval(models.Model):
    sire = models.IntegerField(unique=True)
    nom = models.CharField(max_length = 200)
    race = models.CharField(max_length = 100)
    pedigree = models.CharField(max_length = 500)
    annee_naissance = models.IntegerField()
    photo = models.CharField(max_length = 500)
    embouchure = models.CharField(max_length = 60)
    enrennement = models.CharField(max_length = 60)
    ferrage = models.DateField()
    remarques = models.CharField(max_length = 60)

    def __unicode__(self):
        return "%s %s" % (self.nom, self.sire)

class Discipline_Cheval(models.Model): #affectation de une ou plusieurs disciplines à un cheval
    cheval = models.ForeignKey(Cheval)
    discipline = models.ForeignKey(Discipline)

class Ecurie(models.Model): #journal des entrées sorties des chevaux
    cheval = models.ForeignKey(Cheval)
    date_entree = models.DateField()
    aptitude = models.ForeignKey(Aptitude, default="Apte")
    date_sortie = models.DateField()

class Veterinaire(models.Model):
    siret = models.IntegerField()
    civilite = models.CharField(max_length=3)
    nom = models.CharField(max_length = 60)
    prenom = models.CharField(max_length = 60)
    adresse = models.CharField(max_length=200)
    cp = models.CharField(max_length=5)
    ville = models.CharField(max_length=100)
    tel = models.CharField(max_length=10)
    fax = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10)
    mail = models.CharField(max_length=300)

    def __unicode__(self):
        return "%S %s" % (self.nom, self.prenom)

class Soigneur(models.Model):
    profil = models.ForeignKey(Profil)
    date_debut = models.DateField()
    date_fin = models.DateField()

class Registe_Elevage(models.Model):
    cheval = models.ForeignKey(Cheval)
    date = models.DateField()
    pathologie = models.CharField(max_length = 500)
    acte = models.CharField(max_length = 500)
    veterinaire = models.ForeignKey(Veterinaire)
    soigneur = models.ForeignKey(Soigneur)

    def __unicode__(self):
        return "%s %S" % (self.date, self.cheval)

class Public(models.Model):
    public = models.CharField(max_length = 100)

    def __unicode__(self):
        return "%s" % public

class Monte(models.Model):
    date = models.DateField()
    duree = models.FloatField()
    discipline = models.ForeignKey(Discipline)
    public = models.ForeignKey(Public)
    encadrant = models.ForeignKey(Encadrant)

    def __unicode__(self):
        return "%s %s %s" % (self.date, self.public, self.encadrant)

class Piquet(models.Model):
    monte = models.ForeignKey(Monte)
    cheval = models.ForeignKey(Cheval)

class Piquet_Club(models.Model):
    piquet = models.ForeignKey(Piquet) # tous les id correspondant à une monte pour affecter un cheval à un caalier
    cavalier = models.ForeignKey(Cavalier)
