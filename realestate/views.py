from django.shortcuts import render

from realestate.utils import get_company

# Create your views here.
def home(request):

	return render(request, 'recontent/home.html', {})

def company(request, **kwargs):
	company = get_company(kwargs['slug'])

	return render(request, 'recontent/company.html', {'company':company})