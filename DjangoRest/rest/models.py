import uuid

from django.db import models

# Create your models here.


class PlayerBattingScore(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    team = models.CharField(max_length=100)
    turn = models.CharField(max_length=100)
    rank = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    sixes = models.IntegerField(default=0)
    fours = models.IntegerField(default=0)
    balls = models.IntegerField(default=1)


class PlayerBowlingScore(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    team = models.CharField(max_length=100)
    turn = models.CharField(max_length=100)
    rank = models.IntegerField(default=0)
    overs = models.FloatField(default=0)
    wickets = models.IntegerField(default=0)
    wicket_name = models.JSONField(default=[])