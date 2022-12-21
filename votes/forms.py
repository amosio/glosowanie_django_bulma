from django import forms
from .models import Vote
from options.models import Option



class VoteForm(forms.ModelForm):
    option = forms.ModelChoiceField(queryset=Option.objects.all(), to_field_name="option_name")

    class Meta:
        model = Vote
        exclude = ["created", "modified"]