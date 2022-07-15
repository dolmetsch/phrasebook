from django.contrib.admin import site as admin_site

from .Language import Language, LanguageAdmin
from .Tag import Tag, TagAdmin
from .Chapter import Chapter, ChapterAdmin
from .Phrase import Phrase, PhraseAdmin
from .PhraseAudio import PhraseAudio, PhraseAudioAdmin


def register_model_admins ():
	admin_site.register(Language, LanguageAdmin)
	admin_site.register(Tag, TagAdmin)
	admin_site.register(Chapter, ChapterAdmin)
	admin_site.register(Phrase, PhraseAdmin)
	admin_site.register(PhraseAudio, PhraseAudioAdmin)
