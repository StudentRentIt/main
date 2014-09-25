from django import forms
from django.forms import ModelForm

from search.models import Group

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Fieldset, ButtonHolder


class GroupForm(ModelForm):
    # create or update a group
    name = forms.CharField()
    description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={'placeholder': 'What is the group looking for? (optional)'}
    ))

    class Meta:
        model = Group

    def __init__(self, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset('Give your group a name and description if you\'d like',
                Div('name', 'property', css_class="col-md-12"),
                Div('description', css_class="col-md-12"),
            ),
            ButtonHolder(
                Submit('submit', 'Next Add Members', css_class='btn-brand btn-lg'),
                    css_class="text-center"
            )
        )