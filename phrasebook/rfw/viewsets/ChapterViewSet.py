from rest_framework.viewsets import ReadOnlyModelViewSet as ModelViewSet
from phrasebook.models import Chapter
from ..serializers.ChapterSerializer import ChapterSerializer


class ChapterViewSet(ModelViewSet):
	queryset = Chapter.objects.all()
	serializer_class = ChapterSerializer
