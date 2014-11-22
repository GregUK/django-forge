# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import semantic_version.django_fields
import forge.models
import forge.storage


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, db_index=True)),
                ('desc', models.TextField(db_index=True, blank=True)),
                ('tags', models.TextField(db_index=True, blank=True)),
                ('author', models.ForeignKey(to='forge.Author')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', semantic_version.django_fields.VersionField(max_length=200, db_index=True)),
                ('tarball', models.FileField(storage=forge.storage.ForgeStorage(), upload_to=forge.models.tarball_upload)),
                ('module', models.ForeignKey(related_name='releases', to='forge.Module')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='release',
            unique_together=set([('module', 'version')]),
        ),
        migrations.AlterUniqueTogether(
            name='module',
            unique_together=set([('author', 'name')]),
        ),
    ]
