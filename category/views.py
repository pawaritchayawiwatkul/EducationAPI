from rest_framework.views import Response
from rest_framework.decorators import permission_classes
from rest_framework.viewsets import ViewSet
from category.models import SpeakingPracticeCategory, ListeningPracticeCategory
from category.serializers import SpeakingPracticeCategorySerializers, ListeningPracticeCategorySerializers
from exercise.serializers import ListListeningPracticeSerializers, ListSpeakingPracticeSerializers
# Create your views here.

class CategoryViewSet(ViewSet):
    def retrieve(self, request, code):
        try:
            if code[:2] == "LI": 
                category = ListeningPracticeCategory.objects.prefetch_related("practices").get(code=code)
                ser = ListListeningPracticeSerializers(category.practices, many=True)
                return Response(ser.data)
            else:
                category = SpeakingPracticeCategory.objects.prefetch_related("practices").get(code=code)
                ser = ListSpeakingPracticeSerializers(category.practices, many=True)
                return Response(ser.data)
        except ListeningPracticeCategory.DoesNotExist or SpeakingPracticeCategory.DoesNotExist:
            return Response({'error': 'Does not exist.'}, status=400)

    def list(self, request, category_type):
        if category_type == "listening": 
            categories = ListeningPracticeCategory.objects.all()[:50]
            ser = ListeningPracticeCategorySerializers(categories, many=True)
            return Response(ser.data)
        else:
            categories = SpeakingPracticeCategory.objects.all()[:50]
            ser = SpeakingPracticeCategorySerializers(categories, many=True)
            return Response(ser.data)
