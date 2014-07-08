from django.contrib import admin

<<<<<<< HEAD
from flowreport.models import Report, Audience
=======
from flowreport.models import Report, Audience, PropertyImpression
>>>>>>> 953247464bbd149e315d738b8a76f7bf52aa9a66

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
<<<<<<< HEAD
=======
admin.site.register(PropertyImpression)
>>>>>>> 953247464bbd149e315d738b8a76f7bf52aa9a66
