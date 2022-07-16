from django.contrib.admin import ModelAdmin


class PhraseAudioAdmin (ModelAdmin):
	list_display = (
		'id',
		'phrase',
		'file',
		'user_contributed',
	)

	readonly_fields = (
		'user_contributed',
	)

	ordering = (
		'phrase',
		'file',
	)

	list_filter = (
		'phrase__language',
		'user_contributed',
		'phrase',
	)

	def save_model (self, request, instance, form, change):
		if not instance.pk:
			instance.user_contributed = request.user
		instance.save()

