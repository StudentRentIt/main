from django.shortcuts import render


def home(request):
    # informational page for people looking to become campus ambassadors

    return render(request, "cacontent/home.html", {})


def dashboard(request):
    # place for campus ambassadors to view vital statistics

    return render(request, "cacontent/dashboard.html", {})


def add_property(request):
    '''
    campus ambassadors will be able to add new properties into their
    assigned school list
    '''
    action = 'add'

    return render(request, "cacontent/property.html",
        {'action':action})


def edit_property(request):
    '''
    campus ambassadors will be able to edit existing properties that
    fall into their assigned schools
    '''
    action = 'edit'

    return render(request, "cacontent/property.html",
        {'action':action})


def add_content(request):
    '''
    campus ambassadors will be able to add new content such as articles,
    events and deals
    '''
    action = 'add'

    return render(request, "cacontent/content.html",
        {'action':action})


def edit_content(request):
    '''
    campus ambassadors will be able to edit existing content items that
    fall into their assigned schools
    '''
    action = 'edit'

    return render(request, "cacontent/content.html",
        {'action':action})


def support(request):
    '''
    help for campus ambassadors. Will be FAQ as well as some
    processes
    '''

    return render(request, "cacontent/support.html", {})