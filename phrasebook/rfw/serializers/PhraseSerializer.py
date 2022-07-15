from rest_framework.serializers import ModelSerializer
from phrasebook.models import Phrase
from phrasebook.rfw.serializers.PhraseAudioSerializer import PhraseAudioSerializer


class PhraseSerializer(ModelSerializer):
	class Meta:
		model = Phrase
		exclude = ('created_at', 'updated_at')

	audios = PhraseAudioSerializer(many=True, read_only=True)