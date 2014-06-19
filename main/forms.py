from django import forms
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from main.models import USER_TYPE_CHOICES, BOOL_CHOICES, Property, \
    PropertyReserve, PropertyRoom, PropertyImage, PropertyFavorite, Contact, \
    Event, Deal, Roommate, Article, PropertyVideo, PropertySchedule
from localflavor.us.forms import USZipCodeField

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Fieldset, ButtonHolder, Field


class ContactForm(ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    body = forms.CharField(widget = forms.Textarea())
    email = forms.CharField(label='Your Email')

    class Meta:
        model = Contact
        exclude = ['property']

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Begin contact with the apartment manager... now!',
                Div('first_name', css_class="col-md-3"),
                Div('last_name', css_class="col-md-3"),
                Div('email', css_class="col-md-6"),
                Div('phone_number', css_class="col-md-4"),
                Div('subject', css_class="col-md-8"),
                'body'
            ),
            ButtonHolder(
                Submit('submit', 'Contact Now', css_class='btn-success btn-lg'), css_class="text-center"
            )
        )



class FavoriteForm(ModelForm):
    note = forms.CharField(label='', widget=forms.Textarea())

    class Meta:
        model = PropertyFavorite
        exclude = ['property', 'user']


###### Property Forms ######
'''
For the property forms, we're needing to exclude certain groups of fields
so that we can split up the different types of fields for data entry
'''

#groups of fields to show and or hide on property forms
basic_fields = ['school', 'type', 'title', 'addr', 'city', 'state', 'zip_cd']
hidden_fields = ['user', 'lat', 'long', 'active', 'sponsored', 'initial']
detail_fields = ['lease_type', 'lease_term', 'amenities', 'description', 'special', 'fee_desc']
contact_fields = ['contact_first_name', 'contact_last_name', 'contact_phone', 'contact_email']
business_detail_fields = ['description', 'special',]


class BasicPropertyForm(ModelForm):
    #type =  forms.ChoiceField(choices = property_type_choices)

    zip_cd = USZipCodeField(widget=forms.TextInput(), label="Zip Code")
    addr = forms.CharField(label='Address')

    class Meta:
        model = Property
        fields = basic_fields


class DetailPropertyForm(ModelForm):

    class Meta:
        model = Property
        fields = detail_fields

class BusinessDetailPropertyForm(ModelForm):

    class Meta:
        model = Property
        fields = business_detail_fields


class ContactPropertyForm(ModelForm):

    class Meta:
        model = Property
        fields = contact_fields


class RoomPropertyForm(ModelForm):

    class Meta:
        model = PropertyRoom
        exclude = ['property']


class ImagePropertyForm(ModelForm):

    class Meta:
        model = PropertyImage
        exclude = ['property']


class VideoPropertyForm(ModelForm):

    class Meta:
        model = PropertyVideo
        exclude = ['property']


class ReserveForm(ModelForm):
    felony  = forms.ChoiceField(
                widget=forms.RadioSelect,
                choices=BOOL_CHOICES,
                label="Do you have a felony?")
    evicted = forms.ChoiceField(
                widget=forms.RadioSelect,
                choices=BOOL_CHOICES,
                label="Have you ever been evicted?")
    credit = forms.ChoiceField(
                widget=forms.RadioSelect,
                choices=BOOL_CHOICES,
                label="Do you have decent credit?")
    agree = forms.BooleanField(required=True,
                label= "",
                help_text = "I agree to submit my application, lease and all other documentation to the apartment community or property and pay the fees and deposits indicated in order to guarantee residence.",
                error_messages={'required': 'You must agree to the terms'})


    class Meta:
        model = PropertyReserve
        exclude = ['property', 'user']

    def __init__(self, *args, **kwargs):
        super(ReserveForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.help_text_inline = True
        self.helper.error_text_inline = False
        self.helper.layout = Layout(
            Fieldset(
                'Reserving an apartment has never been easier.',
                Div('first_name', css_class="col-md-3"),
                Div('last_name', css_class="col-md-3"),
                Div('email', css_class="col-md-6"),
                Div('phone_number', css_class="col-md-4"),
                Div(Field('move_in_date', css_class='datepicker'), css_class="col-md-4"),
                Div('floor_plan', css_class="col-md-4"),
                Div(
                    'felony',
                    'evicted',
                    'credit',
                    css_class="col-md-6"
                ),
                Div('agree', css_class="col-md-6"),
            ),
            ButtonHolder(
                Submit('submit', 'Reserve Now', css_class='btn-success btn-lg'), css_class="text-center"
            )
        )


class ScheduleForm(ModelForm):

    class Meta:
        model = PropertySchedule
        exclude = ['property', 'user']

    def __init__(self, *args, **kwargs):
        super(ScheduleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Schedule a tour and find your new pad.',
                Div('first_name', css_class="col-md-3"),
                Div('last_name', css_class="col-md-3"),
                Div('email', css_class="col-md-6"),
                Div('phone_number', css_class="col-md-4"),
                Div(Field('schedule_date', css_class='datepicker'), css_class="col-md-4"),
                Div('schedule_time', css_class="col-md-4"),
            ),
            ButtonHolder(
                Submit('submit', 'Schedule Now', css_class='btn-success btn-lg'),
                css_class="text-center"
            )
        )



##### User Forms #####
class UserCreationFormExtended(UserCreationForm):
    user_type = forms.ChoiceField(required=False, choices=USER_TYPE_CHOICES)

    def __init__(self, *args, **kwargs):
        super(UserCreationFormExtended, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
       model = get_user_model()
       fields = ('username', 'user_type', 'email', 'first_name', 'last_name', 'password1', 'password2')


class UserUpdateForm(ModelForm):
    first_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name", "email")

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Accurate data is important for contacting apartments',
                Div('first_name', css_class="col-md-6"),
                Div('last_name', css_class="col-md-6"),
                Div('email', css_class="col-md-12")
            ),
            ButtonHolder(
                Submit('submit', 'Save', css_class='btn-success btn-lg'), css_class="text-center"
            )
        )


##### School Forms #####
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



class RoommateForm(ModelForm):
    hidden_roommate = forms.IntegerField(widget=forms.HiddenInput, label="",
        required=False)

    class Meta:
        model = Roommate
        exclude = ['school', 'user']