# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'PropertyLeaseStart'
        db.delete_table('main_propertyleasestart')

        # Deleting model 'Amenity'
        db.delete_table('main_amenity')

        # Deleting model 'Property'
        db.delete_table('main_property')

        # Removing M2M table for field lease_term on 'Property'
        db.delete_table(db.shorten_name('main_property_lease_term'))

        # Removing M2M table for field amenities on 'Property'
        db.delete_table(db.shorten_name('main_property_amenities'))

        # Removing M2M table for field lease_type on 'Property'
        db.delete_table(db.shorten_name('main_property_lease_type'))

        # Removing M2M table for field services on 'Property'
        db.delete_table(db.shorten_name('main_property_services'))

        # Deleting model 'PropertyReserve'
        db.delete_table('main_propertyreserve')

        # Deleting model 'School'
        db.delete_table('main_school')

        # Deleting model 'Tag'
        db.delete_table('main_tag')

        # Deleting model 'Deal'
        db.delete_table('main_deal')

        # Deleting model 'Event'
        db.delete_table('main_event')

        # Deleting model 'PropertyVideo'
        db.delete_table('main_propertyvideo')

        # Deleting model 'Article'
        db.delete_table('main_article')

        # Removing M2M table for field tags on 'Article'
        db.delete_table(db.shorten_name('main_article_tags'))

        # Deleting model 'Package'
        db.delete_table('main_package')

        # Removing M2M table for field services on 'Package'
        db.delete_table(db.shorten_name('main_package_services'))

        # Deleting model 'PropertyFavorite'
        db.delete_table('main_propertyfavorite')

        # Deleting model 'Roommate'
        db.delete_table('main_roommate')

        # Deleting model 'PropertyLeaseTerm'
        db.delete_table('main_propertyleaseterm')

        # Deleting model 'Service'
        db.delete_table('main_service')

        # Deleting model 'PropertyRoom'
        db.delete_table('main_propertyroom')

        # Deleting model 'PropertySchedule'
        db.delete_table('main_propertyschedule')

        # Deleting model 'PropertyImage'
        db.delete_table('main_propertyimage')

        # Deleting model 'PropertyLeaseType'
        db.delete_table('main_propertyleasetype')


        # Changing field 'Contact.property'
        db.alter_column('main_contact', 'property_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['property.Property'], null=True))

        # Changing field 'Payment.property'
        db.alter_column('main_payment', 'property_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['property.Property'], null=True))

    def backwards(self, orm):
        # Adding model 'PropertyLeaseStart'
        db.create_table('main_propertyleasestart', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lease_start', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('main', ['PropertyLeaseStart'])

        # Adding model 'Amenity'
        db.create_table('main_amenity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('amenity', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('link', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=100)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(null=True, blank=True, max_length=100)),
            ('special', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('type', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=3)),
        ))
        db.send_create_signal('main', ['Amenity'])

        # Adding model 'Property'
        db.create_table('main_property', (
            ('sponsored', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('type', self.gf('django.db.models.fields.CharField')(default='APT', max_length=20)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('contact_phone', self.gf('localflavor.us.models.PhoneNumberField')(null=True, blank=True, max_length=20)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('state', self.gf('localflavor.us.models.USStateField')(max_length=2)),
            ('package', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Package'], null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lat', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, blank=True, decimal_places=6)),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.School'])),
            ('contact_last_name', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=50)),
            ('contact_first_name', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=50)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('top_list', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('contact_email', self.gf('django.db.models.fields.EmailField')(null=True, blank=True, max_length=75)),
            ('fee_desc', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('addr', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('special', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('zip_cd', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('long', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, blank=True, decimal_places=6)),
        ))
        db.send_create_signal('main', ['Property'])

        # Adding M2M table for field lease_term on 'Property'
        m2m_table_name = db.shorten_name('main_property_lease_term')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('property', models.ForeignKey(orm['main.property'], null=False)),
            ('propertyleaseterm', models.ForeignKey(orm['main.propertyleaseterm'], null=False))
        ))
        db.create_unique(m2m_table_name, ['property_id', 'propertyleaseterm_id'])

        # Adding M2M table for field amenities on 'Property'
        m2m_table_name = db.shorten_name('main_property_amenities')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('property', models.ForeignKey(orm['main.property'], null=False)),
            ('amenity', models.ForeignKey(orm['main.amenity'], null=False))
        ))
        db.create_unique(m2m_table_name, ['property_id', 'amenity_id'])

        # Adding M2M table for field lease_type on 'Property'
        m2m_table_name = db.shorten_name('main_property_lease_type')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('property', models.ForeignKey(orm['main.property'], null=False)),
            ('propertyleasetype', models.ForeignKey(orm['main.propertyleasetype'], null=False))
        ))
        db.create_unique(m2m_table_name, ['property_id', 'propertyleasetype_id'])

        # Adding M2M table for field services on 'Property'
        m2m_table_name = db.shorten_name('main_property_services')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('property', models.ForeignKey(orm['main.property'], null=False)),
            ('service', models.ForeignKey(orm['main.service'], null=False))
        ))
        db.create_unique(m2m_table_name, ['property_id', 'service_id'])

        # Adding model 'PropertyReserve'
        db.create_table('main_propertyreserve', (
            ('felony', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('property', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Property'])),
            ('credit', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('floor_plan', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.PropertyRoom'])),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('phone_number', self.gf('localflavor.us.models.PhoneNumberField')(null=True, max_length=20)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('agree', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('evicted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('reserve_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('move_in_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('main', ['PropertyReserve'])

        # Adding model 'School'
        db.create_table('main_school', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lat', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=6)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.City'], null=True, blank=True)),
            ('link', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=100)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(null=True, max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('mascot', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=50)),
            ('long', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=6)),
        ))
        db.send_create_signal('main', ['School'])

        # Adding model 'Tag'
        db.create_table('main_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('main', ['Tag'])

        # Adding model 'Deal'
        db.create_table('main_deal', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sponsored', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('property', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Property'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(null=True, blank=True, max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.School'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('main', ['Deal'])

        # Adding model 'Event'
        db.create_table('main_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sponsored', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('property', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Property'], null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(null=True, blank=True, max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('time', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.School'])),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('main', ['Event'])

        # Adding model 'PropertyVideo'
        db.create_table('main_propertyvideo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('property', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Property'])),
            ('video_link', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('main', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('main', ['PropertyVideo'])

        # Adding model 'Article'
        db.create_table('main_article', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sponsored', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('property', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Property'], null=True, blank=True)),
            ('create_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(null=True, max_length=100)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('general_page', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.School'], null=True, blank=True)),
        ))
        db.send_create_signal('main', ['Article'])

        # Adding M2M table for field tags on 'Article'
        m2m_table_name = db.shorten_name('main_article_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('article', models.ForeignKey(orm['main.article'], null=False)),
            ('tag', models.ForeignKey(orm['main.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['article_id', 'tag_id'])

        # Adding model 'Package'
        db.create_table('main_package', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('price', self.gf('django.db.models.fields.IntegerField')()),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('similar_property_strength', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('main', ['Package'])

        # Adding M2M table for field services on 'Package'
        m2m_table_name = db.shorten_name('main_package_services')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('package', models.ForeignKey(orm['main.package'], null=False)),
            ('service', models.ForeignKey(orm['main.service'], null=False))
        ))
        db.create_unique(m2m_table_name, ['package_id', 'service_id'])

        # Adding model 'PropertyFavorite'
        db.create_table('main_propertyfavorite', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('note', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('property', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Property'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('main', ['PropertyFavorite'])

        # Adding model 'Roommate'
        db.create_table('main_roommate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('create_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('property', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Property'], null=True, blank=True)),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.School'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(null=True, blank=True, max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(null=True, blank=True, max_length=75)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('phone', self.gf('localflavor.us.models.PhoneNumberField')(null=True, blank=True, max_length=20)),
        ))
        db.send_create_signal('main', ['Roommate'])

        # Adding model 'PropertyLeaseTerm'
        db.create_table('main_propertyleaseterm', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
            ('lease_term', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('lease_term_short', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=5)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('main', ['PropertyLeaseTerm'])

        # Adding model 'Service'
        db.create_table('main_service', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('price', self.gf('django.db.models.fields.IntegerField')()),
            ('service_type', self.gf('django.db.models.fields.CharField')(default='R', max_length=1)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('main', ['Service'])

        # Adding model 'PropertyRoom'
        db.create_table('main_propertyroom', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lease_start', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.PropertyLeaseStart'], default=2)),
            ('property', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Property'])),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('bed_count', self.gf('django.db.models.fields.IntegerField')()),
            ('sq_ft', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('bath_count', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=1)),
        ))
        db.send_create_signal('main', ['PropertyRoom'])

        # Adding model 'PropertySchedule'
        db.create_table('main_propertyschedule', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('create_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('property', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Property'])),
            ('schedule_date', self.gf('django.db.models.fields.DateField')()),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('schedule_time', self.gf('django.db.models.fields.TimeField')()),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('phone_number', self.gf('localflavor.us.models.PhoneNumberField')(null=True, max_length=20)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('main', ['PropertySchedule'])

        # Adding model 'PropertyImage'
        db.create_table('main_propertyimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('property', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Property'])),
            ('order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('main', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('floorplan', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('caption', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=40)),
        ))
        db.send_create_signal('main', ['PropertyImage'])

        # Adding model 'PropertyLeaseType'
        db.create_table('main_propertyleasetype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lease_type', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('main', ['PropertyLeaseType'])


        # Changing field 'Contact.property'
        db.alter_column('main_contact', 'property_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Property'], null=True))

        # Changing field 'Payment.property'
        db.alter_column('main_payment', 'property_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Property'], null=True))

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
            'link': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'state': ('localflavor.us.models.USStateField', [], {'max_length': '2'})
        },
        'main.contact': {
            'Meta': {'object_name': 'Contact'},
            'body': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'contact_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone_number': ('localflavor.us.models.PhoneNumberField', [], {'null': 'True', 'max_length': '20'}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['property.Property']", 'null': 'True', 'blank': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'main.payment': {
            'Meta': {'object_name': 'Payment'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'payment_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['property.Property']", 'null': 'True', 'blank': 'True'}),
            'recurring': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'services': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['property.Service']", 'null': 'True', 'symmetrical': 'False', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'main.teammember': {
            'Meta': {'object_name': 'TeamMember'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'main.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'related_name': "'profile'", 'unique': 'True'}),
            'user_type': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '30'})
        },
        'property.amenity': {
            'Meta': {'ordering': "['amenity']", 'object_name': 'Amenity'},
            'amenity': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'link': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'special': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'type': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '3'})
        },
        'property.package': {
            'Meta': {'ordering': "['-order']", 'object_name': 'Package'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'price': ('django.db.models.fields.IntegerField', [], {}),
            'services': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['property.Service']", 'null': 'True', 'symmetrical': 'False', 'blank': 'True'}),
            'similar_property_strength': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'property.property': {
            'Meta': {'ordering': "['-top_list', '-sponsored', '-package__order', 'id']", 'object_name': 'Property'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'addr': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'amenities': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['property.Amenity']", 'null': 'True', 'symmetrical': 'False', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'null': 'True', 'blank': 'True', 'max_length': '75'}),
            'contact_first_name': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '50'}),
            'contact_last_name': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '50'}),
            'contact_phone': ('localflavor.us.models.PhoneNumberField', [], {'null': 'True', 'blank': 'True', 'max_length': '20'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fee_desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'blank': 'True', 'decimal_places': '6'}),
            'lease_term': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['property.PropertyLeaseTerm']", 'null': 'True', 'symmetrical': 'False', 'blank': 'True'}),
            'lease_type': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['property.PropertyLeaseType']", 'null': 'True', 'symmetrical': 'False', 'blank': 'True'}),
            'long': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'blank': 'True', 'decimal_places': '6'}),
            'package': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['property.Package']", 'null': 'True', 'blank': 'True'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school.School']"}),
            'services': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['property.Service']", 'null': 'True', 'symmetrical': 'False', 'blank': 'True'}),
            'special': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'sponsored': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'state': ('localflavor.us.models.USStateField', [], {'max_length': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'top_list': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'APT'", 'max_length': '20'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'}),
            'zip_cd': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'property.propertyleaseterm': {
            'Meta': {'ordering': "['order']", 'object_name': 'PropertyLeaseTerm'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lease_term': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'lease_term_short': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '5'}),
            'order': ('django.db.models.fields.IntegerField', [], {})
        },
        'property.propertyleasetype': {
            'Meta': {'ordering': "['lease_type']", 'object_name': 'PropertyLeaseType'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lease_type': ('django.db.models.fields.CharField', [], {'max_length': '20'})
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
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.City']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'}),
            'link': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'long': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'}),
            'mascot': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['main']