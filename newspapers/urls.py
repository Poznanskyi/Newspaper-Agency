from django.urls import path, include
from .views import (
    index,
    TopicListView,
    TopicCreateView,
    RedactorListView,
    RedactorDetailView,
    NewspaperDetailView,
    NewspaperCreateView,
    NewspaperUpdateView,
    NewspaperListView,
)

app_name = 'newspapers'

urlpatterns = [
    path("", index, name="index"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', NewspaperListView.as_view(), name='newspaper_list'),
    path('<int:pk>/', NewspaperDetailView.as_view(), name='newspaper_detail'),
    path('topics/', TopicListView.as_view(), name='topic_list'),
    path('topics/create/', TopicCreateView.as_view(), name='topic_create'),
    path('redactors/', RedactorListView.as_view(), name='redactor_list'),
    path('redactors/<int:pk>/', RedactorDetailView.as_view(), name='redactor_detail'),
    path('create/', NewspaperCreateView.as_view(), name='newspaper_create'),
    path('<int:pk>/edit/', NewspaperUpdateView.as_view(), name='newspaper_update'),
]