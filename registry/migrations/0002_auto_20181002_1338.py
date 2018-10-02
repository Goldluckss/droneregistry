# Generated by Django 2.1.2 on 2018-10-02 12:38

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pilot',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('is_active', models.BooleanField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='RpasTest',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('test_type', models.IntegerField(choices=[(0, 'Online Test'), (1, 'In Authorized Test Center'), (2, 'Other')], default=0)),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='RpasTestValidity',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('taken_at', models.DateTimeField(blank=True, null=True)),
                ('expiration', models.DateTimeField(blank=True, null=True)),
                ('pilot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registry.Pilot')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registry.RpasTest')),
            ],
        ),
        migrations.AddField(
            model_name='authorization',
            name='airspace_type',
            field=models.IntegerField(choices=[(0, 'NA'), (1, 'Green'), (2, 'Amber'), (3, 'Red')], default=0),
        ),
        migrations.AddField(
            model_name='authorization',
            name='area_type',
            field=models.IntegerField(choices=[(0, 'Unpopulated'), (1, 'Sparsely Populated'), (2, 'Densely Populated')], default=0),
        ),
        migrations.AddField(
            model_name='authorization',
            name='authorization_type',
            field=models.IntegerField(choices=[(0, 'NA'), (1, 'Light UAS Operator Certificate'), (2, 'Standard Scenario Authorization')], default=0),
        ),
        migrations.AddField(
            model_name='authorization',
            name='operation_max_height',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='authorization',
            name='permit_to_fly_above_crowd',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='authorization',
            name='risk_type',
            field=models.IntegerField(choices=[(0, 'NA'), (1, 'SAIL 1'), (2, 'SAIL 2'), (3, 'SAIL 3'), (4, 'SAIL 4'), (5, 'SAIL 5'), (6, 'SAIL 6')], default=0),
        ),
        migrations.AddField(
            model_name='contact',
            name='social_security_number',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='operator',
            name='vat_number',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='rpas',
            name='is_airworthy',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='authorization',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 0, 0, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='operator',
            name='operator_type',
            field=models.IntegerField(choices=[(0, 'Open'), (1, 'Specific'), (2, 'Certified')], default=0),
        ),
        migrations.AddField(
            model_name='pilot',
            name='operator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registry.Operator'),
        ),
        migrations.AddField(
            model_name='pilot',
            name='tests',
            field=models.ManyToManyField(through='registry.RpasTestValidity', to='registry.RpasTest'),
        ),
    ]
