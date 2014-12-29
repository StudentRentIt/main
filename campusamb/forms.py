from django import forms
from django.forms import ModelForm

from property.models import Property
from blog.models import Article
from school.models import Deal, Event

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
                Submit('submit', 'Save Property', css_class='btn-brand btn-lg'),
                css_class="text-center"
            )
        )


class EditPropertyForm(AddPropertyForm):

    class Meta:
        model = Property
        exclude = ['property', 'user']


class AddDealForm(ModelForm):

    class Meta:
        model = Deal
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(AddDealForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset('',
                Div('title', css_class="col-sm-6"),
                Div('heading', css_class="col-sm-6"),
                Div('description', css_class="col-sm-6"),
                Div('school', css_class="col-sm-3"),
                Div('property', css_class="col-sm-3"),
                Div('image', css_class="col-sm-2"),
                Div('active', css_class="col-sm-2"),
                Div('sponsored', css_class="col-sm-2"),
            ),
            ButtonHolder(
                Submit('submit', 'Save Deal', css_class='btn-brand btn-lg'),
                css_class="text-center"
            )
        )


class AddArticleForm(ModelForm):

    class Meta:
        model = Article
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(AddArticleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset('',
                Div('title', css_class="col-sm-6"),
                Div('heading', css_class="col-sm-6"),
                Div('body', css_class="col-sm-6"),
                Div('school', css_class="col-sm-3"),
                Div('property', css_class="col-sm-3"),
                Div('active', css_class="col-sm-2"),
                Div('sponsored', css_class="col-sm-2"),
                Div('general_page', css_class="col-sm-2"),
                Div('tags', css_class="col-sm-3"),
                Div('image', css_class="col-sm-3"),

            ),
            ButtonHolder(
                Submit('submit', 'Save Article', css_class='btn-brand btn-lg'),
                css_class="text-center"
            )
        )


class AddEventForm(ModelForm):

    class Meta:
        model = Event
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(AddEventForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset('',
                Div('title', css_class="col-sm-6"),
                Div('heading', css_class="col-sm-6"),
                Div('description', css_class="col-sm-6"),
                Div('school', css_class="col-sm-3"),
                Div('property', css_class="col-sm-3"),
                Div('image', css_class="col-sm-2"),
                Div('active', css_class="col-sm-2"),
                Div('sponsored', css_class="col-sm-2"),
                Div('location', css_class="col-sm-6"),
                Div(Field('date', css_class='datepicker')
                    , css_class="col-sm-3"),
                Div('time', css_class="col-sm-3"),

            ),
            ButtonHolder(
                Submit('submit', 'Save Event', css_class='btn-brand btn-lg'),
                css_class="text-center"
            )
        )


class EditArticleForm(AddArticleForm):

    class Meta:
        model = Article
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(EditArticleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()


class EditDealForm(AddDealForm):

    class Meta:
        model = Deal
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(EditDealForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()


class EditEventForm(AddEventForm):

    class Meta:
        model = Event
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(EditEventForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()