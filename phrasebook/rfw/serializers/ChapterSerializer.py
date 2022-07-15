from rest_framework.serializers import ModelSerializer
from phrasebook.models import Chapter


class ChapterSerializer(ModelSerializer):
	class Meta:
		model = Chapter
		exclude = ('created_at', 'updated_at')
