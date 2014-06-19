from django import forms


class DateTimeWidget(forms.DateTimeInput):
    class Media:
        js = ('js/jquery-ui-timepicker-addon.js',)
    def __init__(self, attrs=None):
        if attrs is not None:
            self.attrs = attrs.copy()
        else:
            self.attrs = {'class': 'datetimepicker'}