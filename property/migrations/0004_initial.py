# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Amenity'
        db.create_table('property_amenity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('amenity', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('type', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=3)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(blank=True, null=True, max_length=100)),
            ('link', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=100)),
            ('special', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('property', ['Amenity'])

        # Adding model 'Service'
        db.create_table('property_service', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('price', self.gf('django.db.models.fields.IntegerField')()),
            ('service_type', self.gf('django.db.models.fields.CharField')(default='R', max_length=1)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('property', ['Service'])

        # Adding model 'Package'
        db.create_table('property_package', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('price', self.gf('django.db.models.fields.IntegerField')()),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=0)),
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

        # Adding model 'PropertyLeaseType'
        db.create_table('property_propertyleasetype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lease_type', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('property', ['PropertyLeaseType'])

        # Adding model 'PropertyLeaseTerm'
        db.create_table('property_propertyleaseterm', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lease_term', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('lease_term_short', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=5)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('property', ['PropertyLeaseTerm'])

        # Adding model 'PropertyLeaseStart'
        db.create_table('property_propertyleasestart', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lease_start', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('property', ['PropertyLeaseStart'])

        # Adding model 'Property'
        db.create_table('property_property', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school.School'])),
            ('type', self.gf('django.db.models.fields.CharField')(default='APT', max_length=20)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('addr', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('state', self.gf('localflavor.us.models.USStateField')(max_length=2)),
            ('zip_cd', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('lat', self.gf('django.db.models.fields.DecimalField')(blank=True, max_digits=12, null=True, decimal_places=6)),
            ('long', self.gf('django.db.models.fields.DecimalField')(blank=True, max_digits=12, null=True, decimal_places=6)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('sponsored', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('top_list', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('special', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('fee_desc', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('contact_first_name', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=50)),
            ('contact_last_name', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=50)),
            ('contact_phone', self.gf('localflavor.us.models.PhoneNumberField')(blank=True, null=True, max_length=20)),
            ('contact_email', self.gf('django.db.models.fields.EmailField')(blank=True, null=True, max_length=75)),
            ('package', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['property.Package'], blank=True, null=True)),
        ))
        db.send_create_signal('property', ['Property'])

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

        # Adding model 'PropertyImage'
        db.create_table('property_propertyimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('property', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['property.Property'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('caption', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=40)),
            ('main', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('floorplan', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('order', self.gf('django.db.models.fields.IntegerField')(blank=True, null=True)),
        ))
        db.send_create_signal('property', ['PropertyImage'])

        # Adding model 'PropertyVideo'
        db.create_table('property_propertyvideo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('property', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['property.Property'])),
            ('video_link', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('main', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('order', self.gf('django.db.models.fields.IntegerField')(blank=True, null=True)),
        ))
        db.send_create_signal('property', ['PropertyVideo'])

        # Adding model 'PropertyRoom'
        db.create_table('property_propertyroom', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('property', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['property.Property'])),
            ('lease_start', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['property.PropertyLeaseStart'], default=2)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('bed_count', self.gf('django.db.models.fields.IntegerField')()),
            ('bath_count', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=1)),
            ('sq_ft', self.gf('django.db.models.fields.IntegerField')(blank=True, null=True)),
        ))
        db.send_create_signal('property', ['PropertyRoom'])

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
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('property', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['property.Property'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], blank=True, null=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('phone_number', self.gf('localflavor.us.models.PhoneNumberField')(null=True, max_length=20)),
            ('floor_plan', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['property.PropertyRoom'])),
            ('move_in_date', self.gf('django.db.models.fields.DateField')()),
            ('felony', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('evicted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('credit', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('agree', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('reserve_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('property', ['PropertyReserve'])

        # Adding model 'PropertySchedule'
        db.create_table('property_propertyschedule', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('property', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['property.Property'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], blank=True, null=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('phone_number', self.gf('localflavor.us.models.PhoneNumberField')(null=True, max_length=20)),
            ('create_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('schedule_date', self.gf('django.db.models.fields.DateField')()),
            ('schedule_time', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal('property', ['PropertySchedule'])


    def backwards(self, orm):
        # Deleting model 'Amenity'
        db.delete_table('property_amenity')

        # Deleting model 'Service'
        db.delete_table('property_service')

        # Deleting model 'Package'
        db.delete_table('property_package')

        # Removing M2M table for field services on 'Package'
        db.delete_table(db.shorten_name('property_package_services'))

        # Deleting model 'PropertyLeaseType'
        db.delete_table('property_propertyleasetype')

        # Deleting model 'PropertyLeaseTerm'
        db.delete_table('property_propertyleaseterm')

        # Deleting model 'PropertyLeaseStart'
        db.delete_table('property_propertyleasestart')

        # Deleting model 'Property'
        db.delete_table('property_property')

        # Removing M2M table for field lease_type on 'Property'
        db.delete_table(db.shorten_name('property_property_lease_type'))

        # Removing M2M table for field lease_term on 'Property'
        db.delete_table(db.shorten_name('property_property_lease_term'))

        # Removing M2M table for field amenities on 'Property'
        db.delete_table(db.shorten_name('property_property_amenities'))

        # Removing M2M table for field services on 'Property'
        db.delete_table(db.shorten_name('property_property_services'))

        # Deleting model 'PropertyImage'
        db.delete_table('property_propertyimage')

        # Deleting model 'PropertyVideo'
        db.delete_table('property_propertyvideo')

        # Deleting model 'PropertyRoom'
        db.delete_table('property_propertyroom')

        # Deleting model 'PropertyFavorite'
        db.delete_table('property_propertyfavorite')

        # Deleting model 'PropertyReserve'
        db.delete_table('property_propertyreserve')

        # Deleting model 'PropertySchedule'
        db.delete_table('property_propertyschedule')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'related_name': "'user_set'", 'blank': 'True', 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'related_name': "'user_set'", 'blank': 'True', 'symmetrical': 'False'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'db_table': "'django_content_type'", 'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)", 'object_name': 'ContentType'},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'main.city': {
            'Meta': {'object_name': 'City'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '100'}),
            'multi_university': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'state': ('localflavor.us.models.USStateField', [], {'max_length': '2'})
        },
        'property.amenity': {
            'Meta': {'ordering': "['amenity']", 'object_name': 'Amenity'},
            'amenity': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'null': 'True', 'max_length': '100'}),
            'link': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '100'}),
            'special': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'type': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '3'})
        },
        'property.package': {
            'Meta': {'ordering': "['-order']", 'object_name': 'Package'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'price': ('django.db.models.fields.IntegerField', [], {}),
            'services': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['property.Service']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'similar_property_strength': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'property.property': {
            'Meta': {'ordering': "['-top_list', '-sponsored', '-package__order', 'id']", 'object_name': 'Property'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'addr': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'amenities': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['property.Amenity']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'null': 'True', 'max_length': '75'}),
            'contact_first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '50'}),
            'contact_last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '50'}),
            'contact_phone': ('localflavor.us.models.PhoneNumberField', [], {'blank': 'True', 'null': 'True', 'max_length': '20'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'fee_desc': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'max_digits': '12', 'null': 'True', 'decimal_places': '6'}),
            'lease_term': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['property.PropertyLeaseTerm']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'lease_type': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['property.PropertyLeaseType']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'long': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'max_digits': '12', 'null': 'True', 'decimal_places': '6'}),
            'package': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['property.Package']", 'blank': 'True', 'null': 'True'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school.School']"}),
            'services': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['property.Service']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'special': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'sponsored': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'state': ('localflavor.us.models.USStateField', [], {'max_length': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'top_list': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'APT'", 'max_length': '20'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'}),
            'zip_cd': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'property.propertyfavorite': {
            'Meta': {'object_name': 'PropertyFavorite'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['property.Property']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'property.propertyimage': {
            'Meta': {'ordering': "['-main', 'order', 'caption']", 'object_name': 'PropertyImage'},
            'caption': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '40'}),
            'floorplan': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'main': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'order': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['property.Property']"})
        },
        'property.propertyleasestart': {
            'Meta': {'ordering': "['order']", 'object_name': 'PropertyLeaseStart'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lease_start': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'order': ('django.db.models.fields.IntegerField', [], {})
        },
        'property.propertyleaseterm': {
            'Meta': {'ordering': "['order']", 'object_name': 'PropertyLeaseTerm'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lease_term': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'lease_term_short': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '5'}),
            'order': ('django.db.models.fields.IntegerField', [], {})
        },
        'property.propertyleasetype': {
            'Meta': {'ordering': "['lease_type']", 'object_name': 'PropertyLeaseType'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lease_type': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'property.propertyreserve': {
            'Meta': {'ordering': "['-reserve_date']", 'object_name': 'PropertyReserve'},
            'agree': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'credit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'evicted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'felony': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'floor_plan': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['property.PropertyRoom']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'move_in_date': ('django.db.models.fields.DateField', [], {}),
            'phone_number': ('localflavor.us.models.PhoneNumberField', [], {'null': 'True', 'max_length': '20'}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['property.Property']"}),
            'reserve_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'blank': 'True', 'null': 'True'})
        },
        'property.propertyroom': {
            'Meta': {'ordering': "['price', 'bed_count']", 'object_name': 'PropertyRoom'},
            'bath_count': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '1'}),
            'bed_count': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lease_start': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['property.PropertyLeaseStart']", 'default': '2'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['property.Property']"}),
            'sq_ft': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'})
        },
        'property.propertyschedule': {
            'Meta': {'ordering': "['-create_date']", 'object_name': 'PropertySchedule'},
            'create_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone_number': ('localflavor.us.models.PhoneNumberField', [], {'null': 'True', 'max_length': '20'}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['property.Property']"}),
            'schedule_date': ('django.db.models.fields.DateField', [], {}),
            'schedule_time': ('django.db.models.fields.TimeField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'blank': 'True', 'null': 'True'})
        },
        'property.propertyvideo': {
            'Meta': {'ordering': "['-main', 'order']", 'object_name': 'PropertyVideo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'order': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['property.Property']"}),
            'video_link': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        'property.service': {
            'Meta': {'object_name': 'Service'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.IntegerField', [], {}),
            'service_type': ('django.db.models.fields.CharField', [], {'default': "'R'", 'max_length': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'school.school': {
            'Meta': {'object_name': 'School'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.City']", 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'}),
            'link': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '100'}),
            'long': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'}),
            'mascot': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['property']