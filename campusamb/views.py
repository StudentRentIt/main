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


def content(request):
    # home page for the campus ambassadors

    return render(request, "cacontent/content.html", {})


def support(request):
    # home page for the campus ambassadors

    return render(request, "cacontent/support.html", {})