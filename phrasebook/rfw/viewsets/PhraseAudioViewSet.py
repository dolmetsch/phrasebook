from rest_framework.viewsets import ReadOnlyModelViewSet as ModelViewSet
from phrasebook.models import PhraseAudio
from ..serializers.PhraseAudioSerializer import PhraseAudioSerializer


class PhraseAudioViewSet(ModelViewSet):
	queryset = PhraseAudio.objects.all()
	serializer_class = PhraseAudioSerializer
	filterset_fields = (
		'phrase',
	)