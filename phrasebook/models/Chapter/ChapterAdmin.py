from django.contrib.admin import ModelAdmin


class ChapterAdmin (ModelAdmin):
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
