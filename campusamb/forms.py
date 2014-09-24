from django import forms
from django.forms import ModelForm

from property.models import Property

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Fieldset, ButtonHolder, Field


class AddPropertyForm(ModelForm):

    class Meta:
        model = Property
        exclude = ['property', 'user']

    def __init__(self, *args, **kwargs):
        super(AddPropertyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset('',
                Div('title', css_class="col-sm-6"),
                Div('school', css_class="col-sm-2"),
                Div('neighborhood', css_class="col-sm-2"),
                Div('type', css_class="col-sm-2"),
                Div( # left side div
                    Div('addr', css_class="col-sm-12"),
                    Div('city', css_class="col-sm-6"),
                    Div('state', css_class="col-sm-3"),
                    Div('zip_cd', css_class="col-sm-3"),
                    Div('contact_first_name', css_class="col-sm-6"),
                    Div('contact_last_name', css_class="col-sm-6"),
                    Div('contact_phone', css_class="col-sm-6"),
                    Div('contact_email', css_class="col-sm-6"),
                    css_class="col-sm-6 no-gutter"
                ),
                Div( # right side div
                    Div('active', css_class="col-sm-6"),
                    Div('internal', css_class="col-sm-6"),
                    Div('lease_type', css_class="col-sm-6"),
                    Div('lease_term', css_class="col-sm-6"),
                    css_class="col-sm-6 no-gutter"
                ),
                Div(
                    Div('amenities', css_class="col-sm-3"),
                    Div('description', css_class="col-sm-3"),
                    Div('special', css_class="col-sm-3"),
                    Div('fee_desc', css_class="col-sm-3"),
                    css_class="col-sm-12"
                )

            ),
            ButtonHolder(
                Submit('submit', 'Save Property', css_class='btn-success btn-lg'),
                css_class="text-center"
            )
        )


class EditPropertyForm(AddPropertyForm):

    class Meta:
        model = Property
        exclude = ['property', 'user']


class AddContentForm(ModelForm):

    class Meta:
        model = Property
        exclude = ['property', 'user']

    def __init__(self, *args, **kwargs):
        super(AddContentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()


class EditContentForm(ModelForm):

    class Meta:
        model = Property
        exclude = ['property', 'user']

    def __init__(self, *args, **kwargs):
        super(EditContentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()