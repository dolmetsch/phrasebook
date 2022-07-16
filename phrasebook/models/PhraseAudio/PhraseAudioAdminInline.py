from django.contrib import admin
from .PhraseAudio import PhraseAudio


class PhraseAudioInline(admin.TabularInline):
	model = PhraseAudio

	readonly_fields = (
		'user_contributed',
	)
