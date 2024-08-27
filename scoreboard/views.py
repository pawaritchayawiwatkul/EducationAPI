from rest_framework.views import Response
from rest_framework.decorators import permission_classes
from rest_framework.viewsets import ViewSet
from scoreboard.models import ListeningUserRanking, SpeakingUserRanking, ListeningScoreboard, SpeakingScoreboard
from scoreboard.serializers import RankingSerializer
from exercise.models import SpeakingPractice, ListeningPractice
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
        higher_scores = model.objects.filter(score__gt=score, scoreboard__exercise__code=code).order_by('score')[:5][::-1]
        lower_score = model.objects.filter(score__lte=score, scoreboard__exercise__code=code).order_by('-score')[:6]
        start_rank = model.objects.filter(score__gt=score, scoreboard__exercise__code=code).count() - len(higher_scores) + 1
        ser = RankingSerializer(list(higher_scores) + list(lower_score), many=True)
        print(start_rank)
        result = ser.data
        for r in result:
            r["ranking"] = start_rank
            start_rank += 1
        return Response(result)
    
    def update(self, request, code):
        if code[:2] == "LI":
            model = ListeningUserRanking
            scoreboard_model = ListeningScoreboard
            exercise_model = ListeningPractice
        else: 
            model = SpeakingUserRanking
            scoreboard_model = SpeakingScoreboard
            exercise_model = SpeakingPractice
        score = request.GET.get("score")
        if not score:
            return Response({"error": "Please provide the score"}, status=400)
        try:
            score = int(score)
            try:
                try: 
                    exercise = exercise_model.objects.get(code=code)
                    scoreboard = scoreboard_model.objects.get(exercise__code=code)
                except scoreboard_model.DoesNotExist:
                    scoreboard = scoreboard_model.objects.create(exercise=exercise)
                except exercise_model.DoesNotExist:
                    return Response(status=404)
                exercise.number_of_plays += 1
                exercise.save()
                instance = model.objects.get(user_id=request.user.id, scoreboard_id=scoreboard.id)
                instance.score = score
                instance.save()
                print("PUT")
            except model.DoesNotExist:
                instance = model.objects.create(user_id=request.user.id, score=score, scoreboard_id=scoreboard.id)
                print("POST")
            except scoreboard_model.DoesNotExist:
                return Response(status=400)
            return Response(status=200)
        except ValueError:
            return Response(status=400)
        