from rest_framework import serializers

class RankingSerializer(serializers.Serializer):
    name = serializers.CharField(source="user.full_name")
    score = serializers.IntegerField()

    class Meta:
        fields = ("name", "score")

