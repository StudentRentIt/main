from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render

from property.models import Property
from report.models import PropertyImpression
from report.utils import get_dash_metrics, one_week_ago, one_month_ago, \
						 get_daily_metrics

# Create your views here.
@staff_member_required
def admin_home(request):
	'''
	this is the home dashboard for admins, which currently just means staff.
	Other users that try to access this page will be redirected to login.
	'''
	properties = Property.objects.all()
	daily_metrics = get_daily_metrics(properties)
	dash_metrics = get_dash_metrics(properties)

	return render(request, 'reportcontent/admin_home.html', 
		{'daily_metrics':daily_metrics, 'dash_metrics':dash_metrics})


@login_required
def real_estate_home(request):
	'''
	Home page for real estate users. Any real estate user can access
	this page, and the data will be filtered to their respective properties
	'''
	company = request.user.real_estate_company
	properties = Property.objects.filter(real_estate_company=company, 
		real_estate_company__isnull=False)
	daily_metrics = get_daily_metrics(properties)
	dash_metrics = get_dash_metrics(properties)

	return render(request, 'reportcontent/real_estate_home.html',
		{'daily_metrics':daily_metrics, 'dash_metrics':dash_metrics,
        'company':company})


@login_required
def business_home(request):
	'''
	Home report page for business users. The data in the reports will 
	be filtered to the BUSINESS properties in which they are listed as 
	the owner
	'''
	properties = Property.objects.filter(type="BUS")
	daily_metrics = get_daily_metrics(properties)
	dash_metrics = get_dash_metrics(properties)

	return render(request, 'reportcontent/business_home.html',
		{'daily_metrics':daily_metrics, 'dash_metrics':dash_metrics})

