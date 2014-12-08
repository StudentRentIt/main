# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'PropertyImage'
        db.delete_table('property_propertyimage')

        # Deleting model 'PropertyLeaseType'
        db.delete_table('property_propertyleasetype')

        # Deleting model 'PropertyFavorite'
        db.delete_table('property_propertyfavorite')

        # Deleting model 'PropertyReserve'
        db.delete_table('property_propertyreserve')

        # Deleting model 'PropertyRoom'
        db.delete_table('property_propertyroom')

        # Deleting model 'Package'
        db.delete_table('property_package')

        # Removing M2M table for field services on 'Package'
        db.delete_table(db.shorten_name('property_package_services'))

        # Deleting model 'Service'
        db.delete_table('property_service')

        # Deleting model 'PropertyVideo'
        db.delete_table('property_propertyvideo')

        # Deleting model 'PropertyLeaseTerm'
        db.delete_table('property_propertyleaseterm')

        # Deleting model 'Amenity'
        db.delete_table('property_amenity')

        # Deleting model 'PropertyLeaseStart'
        db.delete_table('property_propertyleasestart')

        # Deleting model 'PropertySchedule'
        db.delete_table('property_propertyschedule')

        # Deleting model 'Property'
        db.delete_table('property_property')

        # Removing M2M table for field amenities on 'Property'
        db.delete_table(db.shorten_name('property_property_amenities'))

        # Removing M2M table for field services on 'Property'
        db.delete_table(db.shorten_name('property_property_services'))

        # Removing M2M table for field lease_type on 'Property'
        db.delete_table(db.shorten_name('property_property_lease_type'))

        # Removing M2M table for field lease_term on 'Property'
        db.delete_table(db.shorten_name('property_property_lease_term'))


    def backwards(self, orm):
        # Adding model 'PropertyImage'
        db.create_table('property_propertyimage', (
            ('property', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['property.Property'])),
            ('floorplan', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('main', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('caption', self.gf('django.db.models.fields.CharField')(blank=True, max_length=40, null=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(blank=True, null=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('property', ['PropertyImage'])

        # Adding model 'PropertyLeaseType'
        db.create_table('property_propertyleasetype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('lease_type', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('property', ['PropertyLeaseType'])

        # Adding model 'PropertyFavorite'
        db.create_table('property_propertyfavorite', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('property', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['property.Property'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('note', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
        ))
        db.send_create_signal('property', ['PropertyFavorite'])

        # Adding model 'PropertyReserve'
        db.create_table('property_propertyreserve', (
            ('credit', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('reserve_date', self.gf('django.db.models.fields.DateField')(blank=True, auto_now_add=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('evicted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('phone_number', self.gf('localflavor.us.models.PhoneNumberField')(max_length=20, null=True)),
            ('agree', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('move_in_date', self.gf('django.db.models.fields.DateField')()),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('property', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['property.Property'])),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('felony', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('floor_plan', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['property.PropertyRoom'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, to=orm['auth.User'], null=True)),
        ))
        db.send_create_signal('property', ['PropertyReserve'])

        # Adding model 'PropertyRoom'
        db.create_table('property_propertyroom', (
            ('bath_count', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=1)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('sq_ft', self.gf('django.db.models.fields.IntegerField')(blank=True, null=True)),
            ('property', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['property.Property'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bed_count', self.gf('django.db.models.fields.IntegerField')()),
            ('lease_start', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['property.PropertyLeaseStart'], default=2)),
        ))
        db.send_create_signal('property', ['PropertyRoom'])

        # Adding model 'Package'
        db.create_table('property_package', (
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('price', self.gf('django.db.models.fields.IntegerField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('similar_property_strength', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('property', ['Package'])

        # Adding M2M table for field services on 'Package'
        m2m_table_name = db.shorten_name('property_package_services')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('package', models.ForeignKey(orm['property.package'], null=False)),
            ('service', models.ForeignKey(orm['property.service'], null=False))
        ))
        db.create_unique(m2m_table_name, ['package_id', 'service_id'])

        # Adding model 'Service'
        db.create_table('property_service', (
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('service_type', self.gf('django.db.models.fields.CharField')(max_length=1, default='R')),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('price', self.gf('django.db.models.fields.IntegerField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('property', ['Service'])

        # Adding model 'PropertyVideo'
        db.create_table('property_propertyvideo', (
            ('main', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(blank=True, null=True)),
            ('property', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['property.Property'])),
            ('video_link', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal('property', ['PropertyVideo'])

        # Adding model 'PropertyLeaseTerm'
        db.create_table('property_propertyleaseterm', (
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lease_term', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('lease_term_short', self.gf('django.db.models.fields.CharField')(blank=True, max_length=5, null=True)),
        ))
        db.send_create_signal('property', ['PropertyLeaseTerm'])

        # Adding model 'Amenity'
        db.create_table('property_amenity', (
            ('special', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('type', self.gf('django.db.models.fields.CharField')(blank=True, max_length=3, null=True)),
            ('amenity', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('link', self.gf('django.db.models.fields.CharField')(blank=True, max_length=100, null=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(blank=True, max_length=100, null=True)),
        ))
        db.send_create_signal('property', ['Amenity'])

        # Adding model 'PropertyLeaseStart'
        db.create_table('property_propertyleasestart', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
            ('lease_start', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('property', ['PropertyLeaseStart'])

        # Adding model 'PropertySchedule'
        db.create_table('property_propertyschedule', (
            ('phone_number', self.gf('localflavor.us.models.PhoneNumberField')(max_length=20, null=True)),
            ('create_date', self.gf('django.db.models.fields.DateField')(blank=True, auto_now_add=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('property', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['property.Property'])),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, to=orm['auth.User'], null=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('schedule_date', self.gf('django.db.models.fields.DateField')()),
            ('schedule_time', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal('property', ['PropertySchedule'])

        # Adding model 'Property'
        db.create_table('property_property', (
            ('type', self.gf('django.db.models.fields.CharField')(max_length=20, default='APT')),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('contact_phone', self.gf('localflavor.us.models.PhoneNumberField')(blank=True, max_length=20, null=True)),
            ('contact_first_name', self.gf('django.db.models.fields.CharField')(blank=True, max_length=50, null=True)),
            ('package', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, to=orm['property.Package'], null=True)),
            ('special', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.School'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('zip_cd', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('state', self.gf('localflavor.us.models.USStateField')(max_length=2)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            ('contact_last_name', self.gf('django.db.models.fields.CharField')(blank=True, max_length=50, null=True)),
            ('addr', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact_email', self.gf('django.db.models.fields.EmailField')(blank=True, max_length=75, null=True)),
            ('sponsored', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('lat', self.gf('django.db.models.fields.DecimalField')(blank=True, max_digits=12, decimal_places=6, null=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('fee_desc', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('long', self.gf('django.db.models.fields.DecimalField')(blank=True, max_digits=12, decimal_places=6, null=True)),
            ('top_list', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('property', ['Property'])

        # Adding M2M table for field amenities on 'Property'
        m2m_table_name = db.shorten_name('property_property_amenities')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('property', models.ForeignKey(orm['property.property'], null=False)),
            ('amenity', models.ForeignKey(orm['property.amenity'], null=False))
        ))
        db.create_unique(m2m_table_name, ['property_id', 'amenity_id'])

        # Adding M2M table for field services on 'Property'
        m2m_table_name = db.shorten_name('property_property_services')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('property', models.ForeignKey(orm['property.property'], null=False)),
            ('service', models.ForeignKey(orm['property.service'], null=False))
        ))
        db.create_unique(m2m_table_name, ['property_id', 'service_id'])

        # Adding M2M table for field lease_type on 'Property'
        m2m_table_name = db.shorten_name('property_property_lease_type')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('property', models.ForeignKey(orm['property.property'], null=False)),
            ('propertyleasetype', models.ForeignKey(orm['property.propertyleasetype'], null=False))
        ))
        db.create_unique(m2m_table_name, ['property_id', 'propertyleasetype_id'])

        # Adding M2M table for field lease_term on 'Property'
        m2m_table_name = db.shorten_name('property_property_lease_term')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('property', models.ForeignKey(orm['property.property'], null=False)),
            ('propertyleaseterm', models.ForeignKey(orm['property.propertyleaseterm'], null=False))
        ))
        db.create_unique(m2m_table_name, ['property_id', 'propertyleaseterm_id'])


    models = {
        
    }

    complete_apps = ['property']