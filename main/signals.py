from django.dispatch import receiver
from django.contrib.auth.models import User

from allauth.socialaccount.models import SocialAccount
from allauth.account.signals import user_signed_up


@receiver(user_signed_up)
def populate_profile(request, sender, **kwargs):
    #Populate local user fields with data from the facebook account
    try:
        facebook_user = SocialAccount.objects.filter(provider='facebook', user_id=request.user.id)
    except:
        facebook_user = None

    if facebook_user:
        #get facebook info
        # fb_username = facebook_user[0].extra_data['username']
        fb_first_name = facebook_user[0].extra_data['first_name']
        fb_last_name = facebook_user[0].extra_data['last_name']

        user = User.objects.get(id=sender.user.id)
        user.first_name = fb_first_name
        user.last_name = fb_last_name
        user.save()
