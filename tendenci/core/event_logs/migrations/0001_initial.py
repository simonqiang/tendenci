# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    depends_on = (
        ('robots', '0001_initial'),
    )

    def forwards(self, orm):
        
        # Adding model 'EventLog'
        db.create_table('event_logs_eventlog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('guid', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'], null=True)),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('entity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entities.Entity'], null=True)),
            ('event_id', self.gf('django.db.models.fields.IntegerField')()),
            ('event_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('event_type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('event_data', self.gf('django.db.models.fields.TextField')()),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('session_id', self.gf('django.db.models.fields.CharField')(max_length=40, null=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True)),
            ('user_ip_address', self.gf('django.db.models.fields.IPAddressField')(max_length=15, null=True)),
            ('server_ip_address', self.gf('django.db.models.fields.IPAddressField')(max_length=15, null=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=255, null=True)),
            ('http_referrer', self.gf('django.db.models.fields.URLField')(max_length=255, null=True)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=120, null=True)),
            ('http_user_agent', self.gf('django.db.models.fields.TextField')(null=True)),
            ('request_method', self.gf('django.db.models.fields.CharField')(max_length=10, null=True)),
            ('query_string', self.gf('django.db.models.fields.TextField')(null=True)),
            ('robot', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['robots.Robot'], null=True)),
            ('create_dt', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('application', self.gf('django.db.models.fields.CharField')(max_length=50, db_index=True)),
            ('action', self.gf('django.db.models.fields.CharField')(max_length=50, db_index=True)),
            ('model_name', self.gf('django.db.models.fields.CharField')(max_length=75)),
        ))
        db.send_create_signal('event_logs', ['EventLog'])

        # Adding model 'EventLogBaseColor'
        db.create_table('event_logs_eventlogbasecolor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('event_id', self.gf('django.db.models.fields.IntegerField')()),
            ('hex_color', self.gf('django.db.models.fields.CharField')(max_length=6)),
        ))
        db.send_create_signal('event_logs', ['EventLogBaseColor'])

        # Adding model 'EventLogColor'
        db.create_table('event_logs_eventlogcolor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event_id', self.gf('django.db.models.fields.IntegerField')()),
            ('hex_color', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('rgb_color', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=11)),
        ))
        db.send_create_signal('event_logs', ['EventLogColor'])


    def backwards(self, orm):
        
        # Deleting model 'EventLog'
        db.delete_table('event_logs_eventlog')

        # Deleting model 'EventLogBaseColor'
        db.delete_table('event_logs_eventlogbasecolor')

        # Deleting model 'EventLogColor'
        db.delete_table('event_logs_eventlogcolor')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 9, 11, 12, 43, 59, 34729)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 9, 11, 12, 43, 59, 34623)'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'entities.entity': {
            'Meta': {'object_name': 'Entity'},
            'admin_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'allow_anonymous_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_anonymous_view': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'allow_member_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_member_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_user_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_user_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'create_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entity_creator'", 'to': "orm['auth.User']"}),
            'creator_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'entity_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'entity_parent_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'entity_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entity_owner'", 'to': "orm['auth.User']"}),
            'owner_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'status_detail': ('django.db.models.fields.CharField', [], {'default': "'active'", 'max_length': '50'}),
            'summary': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'update_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'})
        },
        'event_logs.eventlog': {
            'Meta': {'object_name': 'EventLog'},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'application': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True'}),
            'create_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True'}),
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['entities.Entity']", 'null': 'True'}),
            'event_data': ('django.db.models.fields.TextField', [], {}),
            'event_id': ('django.db.models.fields.IntegerField', [], {}),
            'event_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'event_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'http_referrer': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True'}),
            'http_user_agent': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model_name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'query_string': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'request_method': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'robot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['robots.Robot']", 'null': 'True'}),
            'server_ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True'}),
            'session_id': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'}),
            'user_ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'event_logs.eventlogbasecolor': {
            'Meta': {'object_name': 'EventLogBaseColor'},
            'event_id': ('django.db.models.fields.IntegerField', [], {}),
            'hex_color': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'event_logs.eventlogcolor': {
            'Meta': {'object_name': 'EventLogColor'},
            'event_id': ('django.db.models.fields.IntegerField', [], {}),
            'hex_color': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rgb_color': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '11'})
        },
        'robots.robot': {
            'Meta': {'object_name': 'Robot'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'status_detail': ('django.db.models.fields.CharField', [], {'default': "'active'", 'max_length': '50'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['event_logs']
