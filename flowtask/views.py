#from django.shortcuts import render, get_object_or_404
#from django.contrib.admin.views.decorators import staff_member_required
from django.core.urlresolvers import reverse_lazy
# from django.views.generic import RedirectView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView, MultipleObjectMixin

from flowtask.models import Task
from flowtask.forms import TaskCreateForm, TaskUpdateForm


'''
Tasks is meant to handle tasks throughout any business function.
It is not intended to be added into other apps, however other apps may be
added into flowtask
'''

class TaskListView(ListView):

    model = Task
    template_name = "flowtask/content/task_list.html"


class TaskCreateView(CreateView, MultipleObjectMixin):
    '''
    Update a task. For now we don't load a list and have to render
    a new page. We will want to change that in the future, just creating
    this bandaid because of time constraints.
    '''
    model = Task
    form_class = TaskCreateForm
    template_name = "flowtask/content/task_create.html"
    success_url = reverse_lazy('task-list')
    load_modal = "createTaskModal"
    queryset = Task.objects.all()

    def form_invalid(self, form, **kwargs):
        #need to add in the error status to the context_data
        context = self.get_context_data(**kwargs)
        context['status'] = 'error'
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(TaskCreateView, self).get_context_data(**kwargs)
        context['form'] = self.get_form(self.form_class)
        context['load_modal'] = self.load_modal
        return context


class TaskUpdateView(UpdateView, MultipleObjectMixin):
    '''
    Update a task. For now we don't load a list and have to render
    a new page. We will want to change that in the future, just creating
    this bandaid because of time constraints.
    '''
    model = Task
    template_name = "flowtask/content/task_update.html"
    form_class = TaskUpdateForm
    load_modal = "updateTaskModal"
    object_list = Task.objects.all()
    success_url = reverse_lazy('task-list')
    queryset = Task.objects.all()

    def form_invalid(self, form, **kwargs):
        #need to add in the error status to the context_data
        context = self.get_context_data(**kwargs)
        context['status'] = 'error'
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(TaskUpdateView, self).get_context_data(**kwargs)
        context['load_modal'] = self.load_modal
        return context


class TaskActionListView(TaskUpdateView):
    '''
    Essentially we want this view to display a list of actions that qualify
    under certain criteria. The type of criteria will be passed in through
    the action query parameter
    '''
    template_name = "/flowtask/content/tasks_update.html"