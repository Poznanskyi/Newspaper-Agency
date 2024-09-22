from django.views.generic import ListView
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from .models import Newspaper, Topic, Redactor
from .forms import RedactorSearchForm, NewspaperSearchForm, TopicSearchForm


def index(request):
    context = {
        'num_redactors': Redactor.objects.count(),
        'num_topics': Topic.objects.count(),
        'num_newspapers': Newspaper.objects.count(),
    }
    return render(request, 'newspapers/index.html', context)


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    paginate_by = 10
    template_name = 'newspapers/redactor_list.html'  # Вкажи свій шаблон

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = RedactorSearchForm(initial={"username": username})
        return context

    def get_queryset(self):
        form = RedactorSearchForm(self.request.GET)

        queryset = Redactor.objects.all()
        if form.is_valid() and form.cleaned_data["username"]:
            queryset = queryset.filter(username__icontains=form.cleaned_data["username"])

        return queryset


class NewspaperListView(LoginRequiredMixin, generic.ListView):
    model = Newspaper
    paginate_by = 8
    template_name = 'newspapers/newspaper_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.request.GET.get("title", "")
        context["search_form"] = NewspaperSearchForm(initial={"title": title})
        return context

    def get_queryset(self):
        form = NewspaperSearchForm(self.request.GET)
        queryset = Newspaper.objects.select_related("topic")

        if form.is_valid() and form.cleaned_data["title"]:
            return queryset.filter(title__icontains=form.cleaned_data["title"])

        return queryset

class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    paginate_by = 10  # Кількість тем на сторінці
    template_name = 'your_template_path/topic_list.html'  # Вкажи свій шаблон

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = TopicSearchForm()  # Додай форму для пошуку, якщо потрібно
        return context

    def get_queryset(self):
        queryset = Topic.objects.all()
        # Додатковий код для фільтрації за формою пошуку, якщо вона є
        return queryset

