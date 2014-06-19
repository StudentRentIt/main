from django.db import models
from django.contrib.auth.models import User
# from django.core.urlresolvers import reverse

##### Choices Section #####
TYPE_CHOICES = (
    ('IMP', 'Improvement'),
    ('BUG', 'Software Bug'),
    ('MAI', 'Maintenance'),
)

URGENCY_CHOICES = (
    ('1', 'Emergency'),
    ('2', 'High'),
    ('3', 'Medium'),
    ('4', 'Low'),
)

#if status changes, make sure to change the active/inactive model methods
PROJECT_STATUS_CHOICES = (
    ('PRO', 'Proposed'),
    ('INP', 'In Progress'),
    ('HLD', 'Hold'),
    ('COM', 'Complated'),
    ('CLO', 'Closed'),
)

TASK_STATUS_CHOICES = (
    ('SUB', 'Submitted'),
    ('ASS', 'Assigned'),
    ('INP', 'In Progress'),
    ('PEN', 'Pending'),
    ('CLO', 'Closed'),
    ('COM', 'Completed'),
)


class Project(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    status = models.CharField(max_length=3, default='SUB',
        choices=PROJECT_STATUS_CHOICES)
    create_date = models.DateField(auto_now_add=True)
    complete_date = models.DateField(null=True, blank=True)
    est_hours = models.IntegerField(null=True, blank=True)

    def get_tasks(self):
        Task.objects.filter(project=self)

# Create your models here.
class Task(models.Model):
    project = models.ForeignKey(Project, null=True, blank=True)
    title = models.CharField(max_length=50)
    desc = models.TextField()
    type = models.CharField(max_length=3, default='BUG',
        choices=TYPE_CHOICES)
    urgency = models.CharField(max_length=3, default='4',
        choices=URGENCY_CHOICES)
    status = models.CharField(max_length=3, default='SUB',
        choices=TASK_STATUS_CHOICES)
    est_hours = models.IntegerField(null=True, blank=True)
    note = models.CharField(max_length=500, null=True, blank=True)
    create_date = models.DateField(auto_now_add=True)
    complete_date = models.DateField(null=True, blank=True)
    assigned_to = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        ordering = ['urgency', 'create_date']

    def __str__(self):
        return self.title

    def get_inactive_tasks():
        active_tasks = Task.objects.filter(status__in=['CLO', 'COM'])
        return active_tasks

    def get_active_tasks():
        inactive_tasks = Task.objects.filter(status__in=['SUB', 'PEN', 'IMP', 'ASS'])
        return inactive_tasks


class Change(models.Model):
    task = models.ForeignKey(Task)
    team = models.ManyToManyField(User)
    desk = models.CharField(max_length=500, null=True, blank=True)
    note = models.CharField(max_length=500, null=True, blank=True)
    complete_date = models.DateField(null=True)