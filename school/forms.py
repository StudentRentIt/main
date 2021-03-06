from django import forms
from django.forms import ModelForm

from blog.models import Article
from property.models import Property
from school.models import Event, Deal

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Fieldset, ButtonHolder


class ArticleForm(ModelForm):
    #used to determine that the article form was submitted on a multi-form page
    hidden_article = forms.IntegerField(widget=forms.HiddenInput, label="",
        required=False)
    body = forms.CharField(widget=forms.Textarea(),
                        help_text="Please view our <a href="" >article style guide</a> for help on submission style")
    property = forms.ModelChoiceField(queryset=Property.objects.all().order_by('title'))

    class Meta:
        model = Article
        exclude = ['user', 'school', 'active', 'sponsored', 'general_page']

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Create articles about apartments, events, or anything you\'d like',
                'title',
                'body',
                Div('image', 'property', css_class="col-md-6"),
                Div('tags', css_class="col-md-6")
            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='btn-success btn-lg'), css_class="text-center"
            )
        )


class EventForm(ModelForm):
    hidden_event = forms.IntegerField(widget=forms.HiddenInput, label="",
        required=False)
    property = forms.ModelChoiceField(queryset=Property.objects.all().order_by('title'))

    class Meta:
        model = Event
        exclude = ['user', 'school', 'active', 'sponsored']

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Share events in your apartment, business or school',
                'title',
                'description',
                Div(
                    Div('date',  css_class="col-md-6"),
                    Div('time',  css_class="col-md-6"),
                css_class="row"),
                Div(
                    Div('property',  css_class="col-md-6"),
                    Div('image',  css_class="col-md-6"),
                css_class="row"),
                Div('location')
            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='btn-success btn-lg'), css_class="text-center"
            )
        )


class DealForm(ModelForm):
    hidden_deal = forms.IntegerField(widget=forms.HiddenInput, label="",
        required=False)
    property = forms.ModelChoiceField(queryset=Property.objects.all().order_by('title'))

    class Meta:
        model = Deal
        exclude = ['user', 'school', 'active', 'sponsored']

    def __init__(self, *args, **kwargs):
        super(DealForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Share a deal at your business or apartments',
                'title',
                'description',
                Div(
                    Div('image',  css_class="col-md-6"),
                    Div('property',  css_class="col-md-6"),
                css_class="row")
            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='btn-success btn-lg'), css_class="text-center"
            )
        )