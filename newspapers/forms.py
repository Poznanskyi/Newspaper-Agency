from django import forms


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


class TopicSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="Search by name",
        widget=forms.TextInput(attrs={'placeholder': 'Enter topic name', 'class': 'form-control'
        })
    )