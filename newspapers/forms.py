from django import forms

from django.contrib.auth.forms import UserCreationForm

from newspapers.models import Redactor, Topic, Newspaper


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Redactor
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]


class NewspaperForm(forms.ModelForm):
    publishers = forms.ModelMultipleChoiceField(
        queryset=Redactor.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Choose a publishers",
    )
    topics = forms.ModelMultipleChoiceField(
        queryset=Topic.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Choose a topic",
    )

    class Meta:
        model = Newspaper
        fields = "__all__"


class NewspaperSearchForm(forms.Form):
    title = forms.CharField(max_length=255, required=False, label="")


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ["name"]


class TopicUpdateForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ["name"]
