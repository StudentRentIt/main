from django.shortcuts import render


def home(request):
    # home page for the campus ambassadors

    return render(request, "cacontent/home.html", {})


def dashboard(request):
    # home page for the campus ambassadors

    return render(request, "cacontent/dashboard.html", {})


def property(request):
    # home page for the campus ambassadors

    return render(request, "cacontent/property.html", {})


def school_items(request):
    # home page for the campus ambassadors

    return render(request, "cacontent/school_items.html", {})