from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from property.models import Property
from report.models import PropertyImpression


# Create your views here.
@staff_member_required
def admin_home(request):
	'''
	this is the home dashboard for admins, which currently just means staff.
	Other users that try to access this page will be redirected to login.
	'''
	prop_imps = PropertyImpression.objects.all()

	return render(request, 'reportcontent/admin_home.html', {'prop_imps':prop_imps})

@login_required
def real_estate_home(request):
	'''
	Home page for real estate users. Any real estate user can access
	this page, and the data will be filtered to their respective properties
	'''

	company = request.user.profile.real_estate_company

	prop_imps = PropertyImpression.objects.filter(property__real_estate_company__isnull=False, 
		property__real_estate_company=company)

	return render(request, 'reportcontent/real_estate_home.html',
		{'prop_imps':prop_imps})


@login_required
def business_home(request):
	'''
	Home report page for business users. The data in the reports will 
	be filtered to the BUSINESS properties in which they are listed as 
	the owner
	'''
	business_properties = Property.objects.filter(type="BUS")
	prop_imps = PropertyImpression.objects.filter(property__in=business_properties)

	return render(request, 'reportcontent/business_home.html', 
		{'prop_imps':prop_imps})

