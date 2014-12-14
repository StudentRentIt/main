from django import forms
from django.forms import ModelForm

from property.models import Property,PropertyReserve, PropertyRoom, PropertyImage, \
                            PropertyVideo, PropertySchedule, BOOL_CHOICES
from localflavor.us.forms import USZipCodeField

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Fieldset, ButtonHolder, Field


'''
For the property forms, we're needing to exclude certain groups of fields
so that we can split up the different types of fields for data entry
'''

#groups of fields to show and or hide on property forms
basic_fields = ['school', 'type', 'title', 'addr', 'city', 'state', 'zip_cd']
hidden_fields = ['user', 'lat', 'long', 'active', 'sponsored', 'initial']
detail_fields = ['lease_type', 'lease_term', 'amenities', 'description', 'special', 'fee_desc']
contact_fields = ['contact_user']
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
                'Schedule a tour and find your new pad',
                Div('first_name', css_class="col-md-3"),
                Div('last_name', css_class="col-md-3"),
                Div('email', css_class="col-md-6"),
                Div('phone_number', css_class="col-md-4"),
                Div(Field('schedule_date', css_class='datepicker'), css_class="col-md-4"),
                Div('schedule_time', css_class="col-md-4"),
            ),
            ButtonHolder(
                Submit('submit', 'Schedule Now', css_class='btn-brand btn-lg'),
                css_class="text-center"
            )
        )