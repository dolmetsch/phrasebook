from django.urls import path
from ..views import PhraseListView


urlpatterns = [	
	path('', PhraseListView.as_view()),
	path('<language>/', PhraseListView.as_view()),
]
