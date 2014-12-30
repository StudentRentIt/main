from django import forms
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from main.models import USER_TYPE_CHOICES, Contact
from property.models import PropertyFavorite

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Fieldset, ButtonHolder
from allauth.account import forms as allauthforms


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
                '',
                Div('first_name', css_class="col-md-3"),
                Div('last_name', css_class="col-md-3"),
                Div('email', css_class="col-md-6"),
                Div('phone_number', css_class="col-md-4"),
                Div('subject', css_class="col-md-8"),
                'body'
            ),
            ButtonHolder(
                Submit('submit', 'Send', 
                    css_class='btn-brand btn-lg'), 
                    css_class="text-center"
            )
        )



class FavoriteForm(ModelForm):
    note = forms.CharField(label='', widget=forms.Textarea())

    class Meta:
        model = PropertyFavorite
        exclude = ['property', 'user']



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
    pic = forms.ImageField(required=False)

    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name", "email", "pic")

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Accurate data is important for contacting apartments',
                Div('first_name', css_class="col-sm-6"),
                Div('last_name', css_class="col-sm-6"),
                Div('email', css_class="col-sm-12"),
                Div('pic', css_class="col-sm-12")
            ),
            ButtonHolder(
                Submit('submit', 'Save', css_class='btn-brand btn-lg'), css_class="text-center"
            )
        )

class LoginForm(allauthforms.LoginForm):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                '',
                Div('login'),
                Div('password'),
            ),
            ButtonHolder(
                Submit('submit', 'Sign In', css_class='btn-brand btn-lg'), 
                    css_class="text-center"
            )
        )


class SignupForm(allauthforms.SignupForm):
    #used as a replacement for allauth SignUpForm
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                '',
                Div('username', css_class="col-sm-12"),
                Div('email', css_class="col-sm-12"),
                Div('first_name', css_class="col-sm-6"),
                Div('last_name', css_class="col-sm-6"),
                Div('password1', css_class="col-sm-12"),
                Div('password2', css_class="col-sm-12"),
            ),
            ButtonHolder(
                Submit('submit', 'Sign Up', css_class='btn-brand btn-lg'), 
                    css_class="text-center"
            )
        )

class ResetPasswordForm(allauthforms.ResetPasswordForm):
    
    def __init__(self, *args, **kwargs):
        super(ResetPasswordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                '',
                Div('email', css_class="col-sm-12"),
            ),
            ButtonHolder(
                Submit('submit', 'Reset My Password', css_class='btn-brand btn-lg'), 
                    css_class="text-center"
            )
        )


class ChangePasswordForm(allauthforms.ChangePasswordForm):
    
    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                '',
                Div('password1', css_class="col-sm-12"),
                Div('password2', css_class="col-sm-12"),
            ),
            ButtonHolder(
                Submit('submit', 'Change Password', css_class='btn-brand btn-lg'), 
                    css_class="text-center"
            )
        )

class ResetPasswordKeyForm(allauthforms.ResetPasswordKeyForm):

    def __init__(self, *args, **kwargs):
        super(ResetPasswordKeyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                '',
                Div('password1', css_class="col-sm-12"),
                Div('password2', css_class="col-sm-12"),
            ),
            ButtonHolder(
                Submit('submit', 'Change Password', css_class='btn-brand btn-lg'), 
                    css_class="text-center"
            )
        )

