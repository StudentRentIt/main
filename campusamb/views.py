from django.shortcuts import render, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required

from campusamb.forms import AddPropertyForm, EditPropertyForm
from property.models import Property


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

    return render(request, "cacontent/content.html",
        {'action':action, 'type':type})


@staff_member_required
def edit_content(request):
    '''
    campus ambassadors will be able to edit existing content items that
    fall into their assigned schools
    '''
    action = 'edit'
    form = ""

    return render(request, "cacontent/content.html",
        {'action':action, 'form':form, 'type':type})


@staff_member_required
def manage_content(request):
    '''
    show the content items that the campus ambassador is able to edit
    '''
    action = 'manage'

    return render(request, "cacontent/manage_content.html",
        {'action':action})


@staff_member_required
def support(request):
    '''
    help for campus ambassadors. Will be FAQ as well as some
    processes
    '''

    return render(request, "cacontent/support.html", {})