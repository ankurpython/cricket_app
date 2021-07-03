# Generated by Django 3.2.4 on 2021-07-03 08:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerBattingScore',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('team', models.CharField(max_length=100)),
                ('turn', models.CharField(max_length=100)),
                ('rank', models.IntegerField(default=0)),
                ('score', models.IntegerField(default=0)),
                ('sixes', models.IntegerField(default=0)),
                ('fours', models.IntegerField(default=0)),
                ('balls', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerBowlingScore',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('team', models.CharField(max_length=100)),
                ('turn', models.CharField(max_length=100)),
                ('rank', models.IntegerField(default=0)),
                ('overs', models.FloatField(default=0)),
                ('wickets', models.IntegerField(default=0)),
                ('wicket_name', models.JSONField(default=[])),
            ],
        ),
    ]