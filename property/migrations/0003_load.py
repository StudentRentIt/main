# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'amenity'
        db.rename_table('main_amenity', 'property_amenity')

        # Adding model 'Service'
        db.rename_table('main_service', 'property_service')

        # Adding model 'Package'
        db.rename_table('main_package', 'property_package')


        # Adding M2M table for field services on 'Package'
        db.rename_table('main_package_services', 'property_package_services')

        # m2m_table_name = db.shorten_name('property_package_services')
        # db.create_table(m2m_table_name, (
        #     ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
        #     ('package', models.ForeignKey(orm['property.package'], null=False)),
        #     ('service', models.ForeignKey(orm['property.service'], null=False))
        # ))
        # db.create_unique(m2m_table_name, ['package_id', 'service_id'])

        # Adding model 'PropertyLeaseType'
        db.rename_table('main_propertyleasetype', 'property_propertyleasetype')

        # Adding model 'PropertyLeaseTerm'
        db.rename_table('main_propertyleaseterm', 'property_propertyleaseterm')

        # Adding model 'PropertyLeaseStart'
        db.rename_table('main_propertyleasestart', 'property_propertyleasestart')

        # Adding model 'Property'
        db.rename_table('main_property', 'property_property')

        # Adding M2M table for field lease_type on 'Property'
        db.rename_table('main_property_lease_type', 'property_property_lease_type')

        # m2m_table_name = db.shorten_name('property_property_lease_type')
        # db.create_table(m2m_table_name, (
        #     ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
        #     ('property', models.ForeignKey(orm['property.property'], null=False)),
        #     ('propertyleasetype', models.ForeignKey(orm['property.propertyleasetype'], null=False))
        # ))
        # db.create_unique(m2m_table_name, ['property_id', 'propertyleasetype_id'])

        # Adding M2M table for field lease_term on 'Property'
        db.rename_table('main_property_lease_term', 'property_property_lease_term')

        # m2m_table_name = db.shorten_name('property_property_lease_term')
        # db.create_table(m2m_table_name, (
        #     ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
        #     ('property', models.ForeignKey(orm['property.property'], null=False)),
        #     ('propertyleaseterm', models.ForeignKey(orm['property.propertyleaseterm'], null=False))
        # ))
        # db.create_unique(m2m_table_name, ['property_id', 'propertyleaseterm_id'])

        # Adding M2M table for field amenities on 'Property'
        db.rename_table('main_property_amenities', 'property_property_amenities')

        # m2m_table_name = db.shorten_name('property_property_amenities')
        # db.create_table(m2m_table_name, (
        #     ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
        #     ('property', models.ForeignKey(orm['property.property'], null=False)),
        #     ('amenity', models.ForeignKey(orm['property.amenity'], null=False))
        # ))
        # db.create_unique(m2m_table_name, ['property_id', 'amenity_id'])

        # Adding M2M table for field services on 'Property'
        db.rename_table('main_property_services', 'property_property_services')

        # m2m_table_name = db.shorten_name('property_property_services')
        # db.create_table(m2m_table_name, (
        #     ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
        #     ('property', models.ForeignKey(orm['property.property'], null=False)),
        #     ('service', models.ForeignKey(orm['property.service'], null=False))
        # ))
        # db.create_unique(m2m_table_name, ['property_id', 'service_id'])

        # Adding model 'PropertyImage'
        db.rename_table('main_propertyimage', 'property_propertyimage')

        # db.create_table('property_propertyimage', (
        #     ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        #     ('property', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['property.Property'])),
        #     ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        #     ('caption', self.gf('django.db.models.fields.CharField')(null=True, max_length=40, blank=True)),
        #     ('main', self.gf('django.db.models.fields.BooleanField')(default=False)),
        #     ('floorplan', self.gf('django.db.models.fields.BooleanField')(default=False)),
        #     ('order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        # ))
        # db.send_create_signal('property', ['PropertyImage'])

        # Adding model 'PropertyVideo'
        db.rename_table('main_propertyvideo', 'property_propertyvideo')

        # Adding model 'PropertyRoom'
        db.rename_table('main_propertyroom', 'property_propertyroom')

        # Adding model 'PropertyFavorite'
        db.rename_table('main_propertyfavorite', 'property_propertyfavorite')

        # Adding model 'PropertyReserve'
        db.rename_table('main_propertyreserve', 'property_propertyreserve')

        # Adding model 'PropertySchedule'
        db.rename_table('main_propertyschedule', 'property_propertyschedule')

    def backwards(self, orm):
        pass
