from django.contrib.admin import ModelAdmin

from ..PhraseAudio import PhraseAudio
from ..PhraseAudio.PhraseAudioAdminInline import PhraseAudioInline


class PhraseAdmin (ModelAdmin):
	list_display = (
		'original',
		'transcription',
		'translation',
		'language',
		'chapter',
	)

	list_filter = (
		'language',
		'chapter',
	)

	ordering = (
		'language',
		'chapter',
		'original',
	)

	search_fields = (
		'original',
		'transcription',
		'translation',
	)

	inlines = (
		PhraseAudioInline,
	)

	def save_formset (self, request, form, formset, change):
		def set_user (instance):
			if not instance.pk:
				instance.user_contributed = request.user
			instance.save()

		for form in formset.deleted_forms:
			if form.instance.pk:
				form.instance.delete()

		if formset.model == PhraseAudio:
			instances = formset.save(commit=False)
			for i in instances: # map doesn't work for some reason
				set_user(i)
			formset.save_m2m()
			return instances
		else:
			return formset.save()
