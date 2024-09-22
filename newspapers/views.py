from django.urls import reverse_lazy, reverse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from .models import Newspaper, Topic, Redactor
from .forms import RedactorSearchForm, NewspaperSearchForm, TopicSearchForm, NewspaperForm


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
    template_name = 'newspapers/redactor_list.html'

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


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor
    template_name = 'newspapers/redactor_detail.html'


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


class NewspaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = Newspaper
    template_name = 'newspapers/newspaper_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class NewspaperCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    form_class = NewspaperForm
    template_name = 'newspapers/newspaper_form.html'
    success_url = reverse_lazy("newspapers:newspaper_list")


class NewspaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    form_class = NewspaperForm
    template_name = 'newspapers/newspaper_form.html'

    def get_success_url(self):
        return reverse("newspapers:newspaper_detail", args=(self.get_object().id,))


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    fields = ("name",)
    success_url = reverse_lazy("newspapers:topics")