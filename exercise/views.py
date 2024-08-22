from rest_framework.views import Response
from rest_framework.decorators import permission_classes
from rest_framework.viewsets import ViewSet
from exercise.models import SpeakingPractice, ListeningPractice
from exercise.serializers import SpeakingPracticeDetailSerializers, ListeningPracticeDetailSerializers, ListSpeakingPracticeSerializers, ListListeningPracticeSerializers
# Create your views here.

class ExerciseViewSet(ViewSet):
    def retrieve(self, request, code):
        if code[:2] == "LI": 
            instance = ListeningPractice.objects.prefetch_related("questions").get(code=code)
            ser = ListeningPracticeDetailSerializers(instance=instance)
            return Response(ser.data)
        else:
            instance = SpeakingPractice.objects.prefetch_related("targets").get(code=code)
            ser = SpeakingPracticeDetailSerializers(instance=instance)
            return Response(ser.data)

    def search(self, request):
        query = request.GET.get("query")
        speak_queryset = SpeakingPractice.objects.filter(title__icontains=query)
        speak_ser = ListSpeakingPracticeSerializers(speak_queryset, many=True)
        list_queryset = ListeningPractice.objects.filter(title__icontains=query)
        list_ser = ListListeningPracticeSerializers(list_queryset, many=True)
        return Response({
            "practices": speak_ser.data + list_ser.data
        })
    
    def list(self, request, practice_type):
        if practice_type == "listening": 
            list_queryset = ListeningPractice.objects.all()
            list_ser = ListListeningPracticeSerializers(list_queryset, many=True)
            return Response(list_ser.data)
        else:
            speak_queryset = SpeakingPractice.objects.all()
            speak_ser = ListSpeakingPracticeSerializers(speak_queryset, many=True)
            return Response(speak_ser.data)

    