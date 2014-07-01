# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Deal'
        db.rename_table('main_deal', 'school_deal')

        # Adding model 'Event'
        db. rename_table('main_event', 'school_event')

        # Adding model 'Roommate'
        db. rename_table('main_roommate', 'school_roommate')

        # Adding model 'School'
        db. rename_table('main_school', 'school_school')


    def backwards(self, orm):
        # Adding model 'Deal'
        db.rename_table('school_deal', 'main_deal')

        # Adding model 'Event'
        db.rename_table('school_event', 'main_event')

        # Adding model 'Roommate'
        db.rename_table('school_roommate', 'main_roommate')

        # Adding model 'School'
        db.rename_table('school_school', 'main_school')

