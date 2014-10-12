# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('time_updated', models.DateTimeField(auto_now=True, db_index=True)),
                ('time_published', models.DateTimeField(db_index=True, null=True, blank=True)),
                ('title', models.TextField()),
                ('slug', models.TextField(default=b'', blank=True)),
                ('description', models.TextField(default=b'', blank=True)),
            ],
            options={
                'ordering': ('-time_created',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CoolContent',
            fields=[
                ('content_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='example.Content')),
                ('cool', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('example.content',),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('content_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='example.Content')),
                ('chunks', jsonfield.fields.JSONField(default=[], blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('example.content',),
        ),
        migrations.CreateModel(
            name='SitePush',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_started', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('time_completed', models.DateTimeField(db_index=True, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255)),
                ('polymorphic_ctype', models.ForeignKey(related_name=b'polymorphic_example.tag_set', editable=False, to='contenttypes.ContentType', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='content',
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name=b'polymorphic_example.content_set', editable=False, to='contenttypes.ContentType', null=True),
            preserve_default=True,
        ),
    ]
