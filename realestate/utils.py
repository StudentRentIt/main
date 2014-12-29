from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from main.utils import unslugify
from realestate.models import Company


def get_company(slug):
    '''
    pass in value to return the correct school object
    '''
    re_company = get_object_or_404(Company, name__contains=unslugify(slug))

    return re_company

def user_in_company(user, company):
    '''
    check if a user is in a given company. Can receive a request user so we need
    to get our stored user
    '''
    if user.real_estate_company == company:
        return True
    else:
        return False
