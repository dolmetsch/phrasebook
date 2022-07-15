from django.contrib.admin import ModelAdmin


class LanguageAdmin (ModelAdmin):
	list_display = (
		'name',
		'id',
	)

	ordering = (
		'name',
	)

	search_fields = (
		'name',
	)
