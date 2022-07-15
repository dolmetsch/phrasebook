from rest_framework.serializers import ModelSerializer
from phrasebook.models import Tag


class TagSerializer(ModelSerializer):
	class Meta:
		model = Tag
		exclude = ('created_at', 'updated_at')
