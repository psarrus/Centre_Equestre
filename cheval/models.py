# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date


STATUT_CHOICES = (
    ('1', 'Propriété'),
    ('2', 'Commodat'),
    ('3', 'Pension'),
    ('4', 'Débourrage'),
    ('5', 'Autres'),
)

ACTIVITE_CHOICES = (
    ('1', 'Monte'),
    ('2', 'Élevage'),
)

APTITUDE_CHOICES = (
    ('1', 'Apte'),
    ('2', 'Repos'),
    ('3', 'Infirmerie'),
    ('4', 'Autres'),
)


class Emplacement(models.Model):
    zone    = models.CharField(max_length = 100)
    box     = models.CharField(max_length = 100, unique = True, null = True)

    def __unicode__(self):
        return 'Zone %s - box %s' % (self.zone, self.box)

    def serialize(self):
        return {
            'zone': self.zone,
            'box': self.box,
        }


class Cheval(models.Model):
    sire            = models.IntegerField(unique = True)
    nom             = models.CharField(max_length = 100)
    race            = models.CharField(max_length = 100)
    pedigree        = models.CharField(max_length = 100)
    annee_naissance = models.IntegerField()
    photo           = models.FileField(upload_to = 'photos')
    date_entree     = models.DateField(auto_now_add = True)
    date_sortie     = models.DateField(null = True, blank = True)
    activite        = models.CharField(max_length = 1, choices = ACTIVITE_CHOICES)
    remarques       = models.TextField()
    statut          = models.CharField(max_length = 1, choices = STATUT_CHOICES)
    aptitude        = models.CharField(max_length = 1, choices = APTITUDE_CHOICES, default = '1')
    emplacement     = models.OneToOneField(Emplacement, unique = True)

    class Meta:
        verbose_name_plural = 'Chevaux'

    def get_dernier_soin(self):
        return self.soin_set.filter(acte = 1).order_by('-date').first()

    def get_dernier_vaccin(self):
        return self.soin_set.filter(acte = 2).order_by('-date').first()

    def get_dernier_ferrage(self):
        return self.soin_set.filter(acte = 3).order_by('-date').first()

    def get_derniere_vermifugation(self):
        return self.soin_set.filter(acte = 4).order_by('-date').first()

    def __unicode__(self):
        return self.nom

    def serialize(self):
        return {
            'sire': self.sire,
            'nom': self.nom,
            'race': self.race,
            'pedigree': self.pedigree,
            'annee_naissance': self.annee_naissance,
            'date_entree': self.date_entree,
            'date_sortie': self.date_sortie,
            'activite': self.activite,
            'remarques': self.remarques,
            'statut': self.statut,
            'aptitude': self.aptitude,
            'emplacement': self.emplacement,
        }


@receiver(post_save, sender = Cheval)
def add_cheval_piquet_montoir_staff(sender, instance, created, **kwargs):
    from monte.models import CreneauMontoir, PiquetMontoirStaff
    if not PiquetMontoirStaff.objects.filter(cheval = instance):
        if created and instance.activite == '1' or (created == False and (not instance.date_sortie or instance.date_sortie > date.today())):
            for montoir in CreneauMontoir.objects.all():
                PiquetMontoirStaff.objects.create(montoir = montoir, cheval = instance)


@receiver(post_save, sender = Cheval)
def del_cheval_piquet_montoir_staff(sender, instance, created, **kwargs):
    from monte.models import CreneauMontoir, PiquetMontoirStaff
    if created == False and (instance.date_sortie and instance.date_sortie <= date.today()) or instance.activite == '2':
        for montoir in CreneauMontoir.objects.all():
            PiquetMontoirStaff.objects.filter(cheval = instance).delete()


class Journal(models.Model):
    cheval  = models.ForeignKey(Cheval)
    date    = models.DateField()
    motif   = models.CharField(max_length = 100)
    lieu    = models.CharField(max_length = 100)

    class Meta:
        verbose_name_plural = 'Journaux'

    def __unicode__(self):
        return '%s %s' % (self.cheval.nom, self.lieu)
