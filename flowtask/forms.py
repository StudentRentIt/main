from django import forms

from flowtask.models import Task


class TaskCreateForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea(), label='Description')

    class Meta:
        model = Task
        exclude = ('status', 'assigned_to', 'project', 'complete_date', 'est_hours', 'note')


class TaskUpdateForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea(), label='Description')

    class Meta:
        model = Task
        widgets = {'note': forms.Textarea()}