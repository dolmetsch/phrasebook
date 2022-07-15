from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class PhraseBookConfig(AppConfig):
	name = 'phrasebook'
	verbose_name = _('phrasebook')
