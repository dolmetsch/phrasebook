from django.contrib.admin import ModelAdmin


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
