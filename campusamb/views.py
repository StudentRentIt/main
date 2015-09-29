from django.shortcuts import render, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required

from campusamb.forms import AddPropertyForm, EditPropertyForm, AddEventForm, \
  AddArticleForm, AddDealForm
from property.models import Property
from school.models import Deal, Event
from blog.models import Article


def home(request):
  # informational page for people looking to become campus ambassadors

  return render(request, "cacontent/home.html", {})

@staff_member_required
def dashboard(request):
  # place for campus ambassadors to view vital statistics

  return render(request, "cacontent/dashboard.html", {})


@staff_member_required
def add_property(request):
  '''
  campus ambassadors will be able to add new properties into their
  assigned school list
  '''
  action = 'add'
  form = AddPropertyForm()

  return render(request, "cacontent/property.html",
    {'action':action, 'form':form})


@staff_member_required
def edit_property(request, pk):
  '''
  campus ambassadors will be able to edit existing properties that
  fall into their assigned schools
  '''
  action = 'edit'
  property = get_object_or_404(Property, id=pk)
  form = EditPropertyForm(instance=property)

  return render(request, "cacontent/property.html",
    {'action':action, 'form':form})


@staff_member_required
def manage_property(request):
  '''
  Show the properties that the campus ambassador is able to edit
  '''
  action = "manage"
  property_list = Property.objects.all()

  # TODO: will filter based on the CA's assigned schools instead of all()

  return render(request, "cacontent/manage_property.html",
    {'property_list':property_list, 'action':action})


@staff_member_required
def add_content(request, type):
  '''
  campus ambassadors will be able to add new content such as articles,
  events and deals
  '''
  action = 'add-' + type

  if type == "article":
    form = AddArticleForm()
  elif type == "deal":
    form = AddDealForm()
  elif type == "event":
    form = AddEventForm()

  return render(request, "cacontent/content.html",
    {'action':action, 'type':type, 'form':form})


@staff_member_required
def edit_content(request, **kwargs):
  '''
  campus ambassadors will be able to edit existing content items that
  fall into their assigned schools
  '''
  type = kwargs['type']
  id = kwargs['pk']

  action = 'edit-' + type

  if type == "article":
    article = get_object_or_404(Article, id=id)
    form = AddArticleForm(instance=article)
  elif type == "deal":
    deal = get_object_or_404(Deal, id=id)
    form = AddDealForm(instance=deal)
  elif type == "event":
    event = get_object_or_404(Event, id=id)
    form = AddEventForm(instance=event)

  return render(request, "cacontent/content.html",
    {'action':action, 'form':form, 'type':type})


@staff_member_required
def manage_content(request):
  '''
  show the content items that the campus ambassador is able to edit
  '''
  action = 'manage-content'
  deals = Deal.objects.all()
  events = Event.objects.all()
  articles = Article.objects.all()

  return render(request, "cacontent/manage_content.html",
    {'action':action, 'deals':deals, 'events':events, 'articles':articles})


@staff_member_required
def support(request):
  '''
  help for campus ambassadors. Will be FAQ as well as some
  processes
  '''

  return render(request, "cacontent/support.html", {})