from rest_framework.viewsets import ReadOnlyModelViewSet as ModelViewSet
from phrasebook.models import Language
from ..serializers.LanguageSerializer import LanguageSerializer


class LanguageViewSet(ModelViewSet):
	queryset = Language.objects.all()
	serializer_class = LanguageSerializer
