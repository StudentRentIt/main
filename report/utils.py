import datetime

from django.db.models import Count

from main.models import Contact
from report.models import PropertyImpression
from property.models import PropertySchedule


# date functions used in reporting
today = datetime.date.today()
one_week_ago =  today - datetime.timedelta(days=7)

if today.month == 1:
	# the month is january, increment the year
	one_month_ago = datetime.date(today.year - 1, 12, today.day)
else:
	# subtract a month
	one_month_ago = datetime.date(today.year, today.month-1, today.day)


def get_dash_metrics(properties):
	'''
	return data that is to be used to populate the data in the dashboard
	summary data. We want to get the amount of impressions, contacts and
	schedules for a group of properties
	'''

	imps = PropertyImpression.objects.filter(property__in=properties, 
		imp_date__gt=one_month_ago).count()
	
	contacts = Contact.objects.filter(property__in=properties, 
		contact_date__gt=one_month_ago).count()
	
	schedules = PropertySchedule.objects.filter(property__in=properties, 
		create_date__gt=one_month_ago).count()

	data = {"imps":imps, "contacts":contacts, "schedules":schedules}

	return data


def get_daily_metrics(properties):
	'''
	Get daily data for properties. This data will be passed to all types of users
	and it will be passed a list of properties depending on which type of user is
	accessing the data.
	'''
	imps = PropertyImpression.objects.values('imp_date')\
		.filter(imp_date__gt=one_week_ago, property__in=properties)\
		.order_by('-imp_date')\
		.annotate(count=Count('id'))

	contacts = Contact.objects.values('contact_date')\
		.filter(property__in=properties, contact_date__gt=one_week_ago)\
		.order_by('-contact_date')\
		.annotate(count=Count('id'))

	schedules = PropertySchedule.objects.values('create_date')\
		.filter(property__in=properties, create_date__gt=one_week_ago)\
		.order_by('-create_date')\
		.annotate(count=Count('id'))

	data = {"imps":imps, "contacts":contacts, "schedules":schedules}

	return data
