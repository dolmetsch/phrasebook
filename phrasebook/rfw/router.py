from rest_framework import routers
from .viewsets import *

router = routers.DefaultRouter()

router.register(r'languages', LanguageViewSet)
router.register(r'tags', TagViewSet)
router.register(r'chapters', ChapterViewSet)
router.register(r'phrases', PhraseViewSet)
router.register(r'phrase-audios', PhraseAudioViewSet)
