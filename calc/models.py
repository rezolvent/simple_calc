# -*- coding: utf-8 -*-
from django.db import models


class CalcResult(models.Model):
    result = models.FloatField(verbose_name=u'Результат', editable=False)
    message = models.CharField(max_length=256, verbose_name=u'Сообщение с результатом', editable=False)
    time = models.DateTimeField(verbose_name=u'Время', editable=False, blank=True)

    def __unicode__(self):
        return u"%s (%s)" % (self.result, self.time)

    class Meta:
        ordering = ['time']
