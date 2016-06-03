# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from profil.models import Profil
from cheval.models import Cheval


ACTE_CHOICES = (
    ('1', 'Soin'),
    ('2', 'Vaccin'),
    ('3', 'Ferrage'),
    ('4', 'Vermifugation'),
    ('5', 'Autres'),
)


class Soin(models.Model):
    date        = models.DateField()
    cheval      = models.ForeignKey(Cheval)
    pathologie  = models.CharField(max_length = 100)
    acte        = models.CharField(max_length = 1, choices = ACTE_CHOICES)
    soigneur    = models.ForeignKey(Profil)

    def __unicode__(self):
        return '%s pour %s le %s' % (self.acte, self.cheval, self.date)
