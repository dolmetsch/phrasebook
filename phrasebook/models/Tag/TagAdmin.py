from django.contrib.admin import ModelAdmin


class TagAdmin (ModelAdmin):
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
