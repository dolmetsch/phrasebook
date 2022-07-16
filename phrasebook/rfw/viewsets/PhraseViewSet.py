from rest_framework.viewsets import ReadOnlyModelViewSet as ModelViewSet
from phrasebook.models import Phrase
from ..serializers.PhraseSerializer import PhraseSerializer


class PhraseViewSet(ModelViewSet):
	queryset = Phrase.objects.all()
	serializer_class = PhraseSerializer
	filterset_fields = (
		'language',
		'tags',
		'chapter',
	)
