from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from newspapers.models import Redactor, Newspaper, Topic
from newspapers.forms import (
    RegistrationForm,
    TopicForm,
    TopicUpdateForm,
    NewspaperForm,
    NewspaperSearchForm,
)


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
    else:
        form = RegistrationForm()

    return render(request, "registration/register.html", {"form": form})


class PostSearchView(generic.ListView):
    model = Newspaper
    template_name = "newspapers/newspaper_list.html"
    paginate_by = 8

    def get_queryset(self):
        query = self.request.GET.get("q")
        if not query:
            return Newspaper.objects.none()
        return Newspaper.objects.filter(
            Q(title__icontains=query)
            | Q(content__icontains=query)
            | Q(topics__name__icontains=query)
            | Q(publishers__username__icontains=query)
        ).distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q")
        return context


def index(request):
    num_posts = Newspaper.objects.count()
    num_topics = Topic.objects.count()
    num_redactors = Redactor.objects.count()
    context = {
        "num_posts": num_posts,
        "num_redactors": num_redactors,
        "num_topics": num_topics,
    }

    return render(request, "newspapers/index.html", context=context)


class PostsListView(generic.ListView):
    model = Newspaper
    paginate_by = 8


class PostsCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    form_class = NewspaperForm
    success_url = reverse_lazy("newspapers:posts-list")


class PostsUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    form_class = NewspaperForm

    def get_success_url(self):
        pk = self.kwargs.get("pk")
        return reverse_lazy("newspapers:posts-detail", kwargs={"pk": pk})


class PostsDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("newspapers:posts-list")


class PostsDetailView(generic.DetailView):
    model = Newspaper


class TopicsListView(generic.ListView):
    model = Topic
    paginate_by = 8


class TopicsCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    form_class = TopicForm
    success_url = reverse_lazy("newspapers:topic-list")

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object = form.save()
        newspapers = form.cleaned_data.get("newspapers")
        if newspapers:
            valid_newspapers = [
                newspaper for newspaper in newspapers if
                Newspaper.objects.filter(pk=newspaper.pk).exists()
            ]
            self.object.newspapers.add(*valid_newspapers)

        return response


class TopicsUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    form_class = TopicUpdateForm

    def get_success_url(self):
        pk = self.kwargs.get("pk")
        return reverse_lazy("newspapers:topic-detail", kwargs={"pk": pk})


class TopicsDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("newspapers:topic-list")


class TopicsDetailView(generic.DetailView):
    model = Topic


def custom_404(request, exception):
    context = {"title": "Page not found", "error": f"Not found {request.path}"}
    return render(request, "404.html", context=context, status=404)


class NewspaperListView(LoginRequiredMixin, generic.ListView):
    model = Newspaper
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.request.GET.get("title", "")
        context["search_form"] = NewspaperSearchForm(initial={"title": title})
        return context

    def get_queryset(self):
        form = NewspaperSearchForm(self.request.GET)

        queryset = super().get_queryset().select_related("topic")
        if form.is_valid():
            return queryset.filter(title__icontains=form.cleaned_data["title"])
        return queryset


class NewspaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = Newspaper


class NewspaperCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    form_class = NewspaperForm
    success_url = reverse_lazy("newspapers:newspapers")


class NewspaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    form_class = NewspaperForm

    def get_success_url(self):
        return reverse(
            "newspapers:newspaper-detail", args=(self.get_object().id,)
        )