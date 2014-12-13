import datetime

from report.models import PropertyImpression


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

	imps = PropertyImpression.objects.filter(property__in=properties, imp_date__gt=one_month_ago)\
		.count()

	data = {
		"imps":imps,
		"contacts":0,
		"schedules":0,
	}

	return data