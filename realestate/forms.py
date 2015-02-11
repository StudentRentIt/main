from django import forms
from django.forms import ModelForm
from django.contrib.auth import get_user_model

from .models import Company

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Fieldset, ButtonHolder


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        exclude = ['slug']

    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        
        instance = kwargs.pop('instance')
        self.fields['contact'].queryset = get_user_model().objects.filter(real_estate_company=instance)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset('Edit the information about your company',
                Div(
                    'name',
                    css_class="col-sm-6"
                ),
                Div(
                    'default_school',
                    css_class="col-sm-6"
                ),
                Div(
                    'contact',
                    css_class="col-sm-6"
                ),
                Div(
                    'logo',
                    css_class="col-sm-6"
                ),
            ),
            ButtonHolder(
                Submit('submit', 'Update', css_class='btn-brand btn-lg'), css_class="text-center"
            )
        )