from django.shortcuts import render

# Create your views here.
def admin_home(request):

	return render(request, 'reportcontent/admin_home.html', {})


def real_estate_home(request):

	return render(request, 'reportcontent/real_estate_home.html', {})


def business_home(request):

	return render(request, 'reportcontent/business_home.html', {})