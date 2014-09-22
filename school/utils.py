from django.shortcuts import get_object_or_404

from school.models import School
from main.utils import unslugify


def get_school(slug):
    '''
    pass in value to return the correct school object
    '''
    school = get_object_or_404(School, name__contains=unslugify(slug))

    return school

