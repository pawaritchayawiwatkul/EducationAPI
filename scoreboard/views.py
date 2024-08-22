from rest_framework.views import Response
from rest_framework.decorators import permission_classes
from rest_framework.viewsets import ViewSet
from scoreboard.models import ListeningUserRanking, SpeakingUserRanking, ListeningScoreboard, SpeakingScoreboard
from scoreboard.serializers import RankingSerializer
from rest_framework.permissions import IsAuthenticated
from django.db import models
# Create your views here.

@permission_classes([IsAuthenticated])
class ScoreboardViewSet(ViewSet):
    def retrieve(self, request, code):
        if code[:2] == "LI":
            model = ListeningUserRanking
        else: 
            model = SpeakingUserRanking
        score = model.objects.values("score").get(scoreboard__exercise__code=code, user_id=request.user.id)["score"]
        higher_scores = model.objects.filter(score__gte=score).order_by('-score')[:6][::-1]
        lower_score = model.objects.filter(score__lte=score).exclude(user_id=request.user.id).order_by('score')[:5]
        start_rank = model.objects.filter(score__gt=score).count() - len(higher_scores) + 2
        ser = RankingSerializer(list(higher_scores) + list(lower_score), many=True)
        result = ser.data
        for r in result:
            r["ranking"] = start_rank
            start_rank += 1
        return Response(result)
    
    def update(self, request, code):
        if code[:2] == "LI":
            model = ListeningUserRanking
            scoreboard_model = ListeningScoreboard
        else: 
            model = SpeakingUserRanking
            scoreboard_model = SpeakingScoreboard
        score = request.GET.get("score")
        if not score:
            return Response({"error": "Please provide the score"}, status=400)
        try:
            score = int(score)
            try:
                scoreboard, _ = scoreboard_model.objects.get_or_create(exercise__code=code)
                instance = model.objects.get(user_id=request.user.id, scoreboard_id=scoreboard.id)
                instance.score = score
                instance.save()
            except model.DoesNotExist:
                instance = model.objects.create(user_id=request.user.id, score=score, scoreboard_id=scoreboard.id)
            except scoreboard_model.DoesNotExist:
                return Response(status=400)
            return Response(status=200)
        except ValueError:
            return Response(status=400)
        