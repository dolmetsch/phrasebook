from rest_framework.serializers import ModelSerializer
from phrasebook.models import PhraseAudio


class PhraseAudioSerializer(ModelSerializer):
	class Meta:
		model = PhraseAudio
		exclude = ('created_at', 'updated_at')
