from django.shortcuts import get_object_or_404

from main.utils import unslugify
from realestate.models import Company


def get_company(slug):
    '''
    pass in value to return the correct school object
    '''
    re_company = get_object_or_404(Company, name__contains=unslugify(slug))

    return re_company