from rest_framework.serializers import ModelSerializer
from phrasebook.models import Language


class LanguageSerializer(ModelSerializer):
	class Meta:
		model = Language
		exclude = ('created_at', 'updated_at')
