from django.urls import path, include
from .views import NewspaperListView, TopicListView, RedactorListView

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('newspapers/', NewspaperListView.as_view(), name='newspaper_list'),
    path('topics/', TopicListView.as_view(), name='topic_list'),
    path('redactors/', RedactorListView.as_view(), name='redactor_list'),
]