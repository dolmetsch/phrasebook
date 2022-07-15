from django.db import models
from django.utils.translation import gettext_lazy as _
from ..AbstractModel.AbstractModel import AbstractModel


class Chapter (AbstractModel):

	class Meta:
		verbose_name = _('chapter')
		verbose_name_plural = _('chapters')

	name = models.CharField(
		max_length = 255,
		null = False,
		blank = False,
		verbose_name = _('name'),
	)

	def __str__ (self):
		return self.name
