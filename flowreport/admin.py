from django.contrib import admin

from flowreport.models import Report, Audience

class CommonMedia:
  js = (
    'https://ajax.googleapis.com/ajax/libs/dojo/1.6.0/dojo/dojo.xd.js',
    '/static/js/plugins/dojo-editor.js',
  )
  css = {
    'all': ('/static/css/dojo-editor.css',),
  }


# Register your models here.
admin.site.register(Report, Media = CommonMedia)
admin.site.register(Audience)
