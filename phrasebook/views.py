from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from .models import Language, Phrase


class PhraseListView(ListView):
	model = Phrase
	context_object_name = 'phrases'

	def get_queryset(self):
		language_id = self.kwargs.get('language')
		if language_id:
			self.language = get_object_or_404(
				Language,
				id = self.kwargs['language']
			)
			return Phrase.objects.filter(
				language = self.language
			)
		else:
			return Phrase.objects.all()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		try:
			context['language'] = self.language
		except AttributeError:
			pass
		return context
