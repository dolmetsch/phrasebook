from django.contrib.admin import ModelAdmin


class PhraseAudioAdmin (ModelAdmin):
	list_display = (
		'file',
		'phrase',
		'id',
	)

	ordering = (
		'phrase',
		'file',
	)

	list_filter = (
		'phrase',
		'phrase__language',
	)
