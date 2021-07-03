from django.db.models import F, Sum
from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from rest_framework.response import Response

from rest.models import PlayerBattingScore, PlayerBowlingScore
from rest.serializers import BattingScoreSerializers, BowlingScoreSerializers


class BattingPlayerScore(viewsets.ModelViewSet):
    serializer_class = BattingScoreSerializers
    queryset = PlayerBattingScore.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        balls = PlayerBattingScore.objects.filter(team=data['team']).aggregate(Sum('balls'))
        # make a condition for 5 overs in batting field.
        if balls['balls__sum']:
            balls = balls['balls__sum']
        else:
            balls = 0

        if int(balls) + int(data['balls']) <= 30:
            obj = BattingScoreSerializers(data=data)
            if obj.is_valid():
                obj.save()
                return Response({'status': 'success', 'code': 200})
        return Response({'status': 'all overs completed', 'code': 400})

    def update(self, request, *args, **kwargs):
        data = request.data
        instance = self.get_object()

        balls = PlayerBattingScore.objects.filter(team=instance.team).aggregate(Sum('balls'))

        if int(balls['balls__sum']) + int(data['balls']) <= 30:
            PlayerBattingScore.objects.filter(id=instance.id).update(
                rank=data['rank'],
                score=F('score') + data['score'],
                sixes=F('sixes') + data['sixes'],
                fours=F('fours') + data['fours'],
                balls=F('balls') + data['balls']
            )
            return Response({'status': 'success', 'code': 200})
        return Response({'status': 'all overs completed', 'code': 400})


class BowlingPlayerScore(viewsets.ModelViewSet):
    serializer_class = BowlingScoreSerializers
    queryset = PlayerBowlingScore.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        overs = PlayerBowlingScore.objects.filter(team=data['team']).aggregate(Sum('overs'))
        # make a condition for 5 overs in bowling field.
        if overs['overs__sum']:
            overs = overs['overs__sum']
        else:
            overs = 0

        print(float(overs) + float(data['overs']))
        if float(overs) + float(data['overs']) <= 5:
            obj = BowlingScoreSerializers(data=data)
            if obj.is_valid():
                obj.save()
                return Response({'status': 'success', 'code': 200})
        return Response({'status': 'all overs completed', 'code': 400})

    def update(self, request, *args, **kwargs):
        data = request.data
        instance = self.get_object()
        overs = PlayerBattingScore.objects.filter(team=instance.team).aggregate(Sum('overs'))

        if float(overs['overs__sum']) + float(data['overs']) <= 5:
            obj = PlayerBowlingScore.objects.get(id=instance.id)
            obj.rank = data['rank']
            obj.overs = data['overs']
            obj.wickets += int(data['wickets'])
            obj.wicket_name.append(data['wicket_name'])
            obj.save()
            return Response({'status': 'success', 'code': 200})
        return Response({'status': 'all overs completed', 'code': 400})


class MatchScore(viewsets.ViewSet):
    def list(self, request):
        obj = PlayerBattingScore.objects.values_list('team').distinct()

        score = []
        for i in obj:
            obj = PlayerBattingScore.objects.filter(team=i[0])
            sr = obj.aggregate(Sum('score'))

            obj = PlayerBowlingScore.objects.filter(team=i[0])
            ov = obj.aggregate(Sum('overs'))
            wk = obj.aggregate(Sum('wickets'))

            if sr['score__sum']:
                sr = int(sr['score__sum'])
            else:
                sr = 0

            if ov['overs__sum']:
                ov = float(ov['overs__sum'])
            else:
                ov = 0.0

            if wk['wickets__sum']:
                wk = float(wk['wickets__sum'])
            else:
                wk = 0

            score.append((i[0], [sr, ov, wk]))

        try:
            if score[0][1][1] >= 5 or score[0][1][2] == 10 and score[1][1][1] >= 5 or score[1][1][2] == 10:
                if score[0][1][0] > score[1][1][0]:
                    result = f"{score[0][0]} is winner!"
                else:
                    result = f"{score[1][0]} is winner!"
            else:
                result = "playing"

            dt = {
                "result": result,
                score[0][0]: {"score": score[0][1][0], "overs": score[1][1][1], "wickets": score[1][1][2]},
                score[1][0]: {"score": score[1][1][0], "overs": score[0][1][1], "wickets": score[0][1][2]},
            }

            return Response(dt)
        except:
            return Response({"result": "playing"})
