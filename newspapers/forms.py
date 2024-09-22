from django import forms
from .models import Newspaper, Redactor


class RedactorSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="Search by username",
        widget=forms.TextInput(attrs={'placeholder': 'Enter username', 'class': 'form-control'})
    )


class NewspaperSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="Search by title",
        widget=forms.TextInput(attrs={'placeholder': 'Enter title', 'class': 'form-control'})
    )


class NewspaperForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={"rows": 10, "class": "form-control"}))
    publishers = forms.ModelMultipleChoiceField(
        queryset=Redactor.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-check"}),
    )

    class Meta:
        model = Newspaper
        fields = ['title', 'content', 'topic', 'publishers']


class TopicSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="Search by name",
        widget=forms.TextInput(attrs={'placeholder': 'Enter topic name', 'class': 'form-control'
        })
    )