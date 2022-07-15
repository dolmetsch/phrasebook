from rest_framework import routers
from .viewsets import *

router = routers.DefaultRouter()

router.register(r'languages', LanguageViewSet)
router.register(r'tag', TagViewSet)
router.register(r'chapter', ChapterViewSet)
router.register(r'phrase', PhraseViewSet)
router.register(r'phrase-audios', PhraseAudioViewSet)
