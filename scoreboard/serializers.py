from rest_framework import serializers

class RankingSerializer(serializers.Serializer):
    name = serializers.CharField(source="user.full_name")
    uuid = serializers.CharField(source="user.uuid")
    score = serializers.IntegerField()

    class Meta:
        fields = ("name", "score", "uuid")

