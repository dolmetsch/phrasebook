from django.db import models
from django.utils.translation import gettext_lazy as _
from ..AbstractModel.AbstractModel import AbstractModel


class Phrase (AbstractModel):

	class Meta:
		verbose_name = _('phrase')
		verbose_name_plural = _('phrases')
		unique_together = (
			('language', 'original',),
		)

	original = models.CharField(
		max_length = 255,
		null = False,
		blank = False,
		verbose_name = _('original'),
	)

	transcription = models.CharField(
		max_length = 255,
		null = False,
		blank = False,
		verbose_name = _('transcription'),
	)

	translation = models.CharField(
		max_length = 255,
		null = False,
		blank = False,
		verbose_name = _('translation'),
	)

	language = models.ForeignKey(
		to = 'Language',
		null = False,
		blank = False,
		verbose_name = _('language'),
		on_delete = models.PROTECT,
		related_name = 'phrases',
	)

	chapter = models.ForeignKey(
		to = 'Chapter',
		null = True,
		blank = True,
		verbose_name = _('chapter'),
		on_delete = models.PROTECT,
		related_name = 'phrases',
	)

	tags = models.ManyToManyField(
		to = 'Tag',
		blank = True,
		verbose_name = _('tags'),
		related_name = 'phrases',
	)

	def __str__ (self):
		return f"{self.original} ({self.language})"
