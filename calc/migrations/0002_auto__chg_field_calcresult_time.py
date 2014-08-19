# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'CalcResult.time'
        db.alter_column(u'calc_calcresult', 'time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True))

    def backwards(self, orm):

        # Changing field 'CalcResult.time'
        db.alter_column(u'calc_calcresult', 'time', self.gf('django.db.models.fields.TimeField')(auto_now=True, auto_now_add=True))

    models = {
        u'calc.calcresult': {
            'Meta': {'ordering': "['time']", 'object_name': 'CalcResult'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'result': ('django.db.models.fields.FloatField', [], {}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['calc']