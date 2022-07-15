from rest_framework.viewsets import ReadOnlyModelViewSet as ModelViewSet
from phrasebook.models import Tag
from ..serializers.TagSerializer import TagSerializer


class TagViewSet(ModelViewSet):
	queryset = Tag.objects.all()
	serializer_class = TagSerializer
