from django.db import models
from django.utils.translation import gettext_lazy as _
from ..AbstractModel.AbstractModel import AbstractModel


class PhraseAudio (AbstractModel):

	class Meta:
		verbose_name = _('phrase audio')
		verbose_name_plural = _('phrase audios')

	phrase = models.ForeignKey(
		to = 'Phrase',
		null = False,
		blank = False,
		verbose_name = _('phrase'),
		on_delete = models.PROTECT,
		related_name = 'audios',
	)

	file = models.FileField(
		null = False,
		blank = False,
		verbose_name = _('file'),
		upload_to = 'uploads/phrase_audios/'
	)

	def __str__ (self):
		return f"{self.phrase} - {self.file}"
