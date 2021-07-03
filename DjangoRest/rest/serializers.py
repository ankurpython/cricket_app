from rest_framework import serializers

from rest.models import PlayerBattingScore, PlayerBowlingScore


class BattingScoreSerializers(serializers.ModelSerializer):
    class Meta:
        model = PlayerBattingScore
        fields = '__all__'


class BowlingScoreSerializers(serializers.ModelSerializer):
    class Meta:
        model = PlayerBowlingScore
        fields = '__all__'
