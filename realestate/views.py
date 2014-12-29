from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView

from .models import Company
from .utils import user_in_company
from property.models import Property
        

def home(request):
    '''
    This will be informative information for real estate companies that might want 
    to join us.
    '''

    return render(request, 'recontent/home.html', {})


def company_home(request, **kwargs):
    '''
    home page for a real estate company. Might show show some stats or general
    information
    '''
    slug = kwargs["slug"]
    company = Company.objects.get(slug=slug)

    if user_in_company(request.user, company):
        agents = User.objects.filter(real_estate_company=company)
        page = "home"

        return render(request, 'recontent/company_home.html', 
            {'company':company, 'agents':agents, 'page':page})
    else:
        return render(request, 'recontent/access_denied.html', 
            {'company':company})


def company_members(request, **kwargs):
    '''
    place for real estate companies to manage their members
    '''
    slug = kwargs["slug"]
    company = Company.objects.get(slug=slug)

    if user_in_company(request.user, company):
        template_name = 'recontent/members.html'
        page = "members"

        User = get_user_model()
        members = User.objects.filter(real_estate_company=company)
        
        context = {
            'company':company, 
            'members':members, 
            'page':page
        }

        if request.method == "POST":
            '''
            On the post we are going to either add or remove members
            '''
            
            if "remove" in request.POST["submit"]:
                # receive a post button with value "remove(@user_id)"
                user_id = int(request.POST["submit"].strip("remove"))
                user = User.objects.get(id=user_id)
                user.real_estate_company = None
            elif request.POST["submit"] == "add":
                try:
                    username = request.POST["username"]
                    user = User.objects.get(username=username)
                    user.real_estate_company = company
                except User.DoesNotExist:
                    context['error_msg'] = username + " does not exist"
                    return render(request, template_name, context)

            user.save()

        return render(request, template_name, context)
    else:
        return render(request, 'recontent/access_denied.html', 
            {'company':company})


def company_properties(request, **kwargs):
    '''
    Allow real estate users to edit properties as well as see their search 
    page
    '''
    slug = kwargs["slug"]
    company = Company.objects.get(slug=slug)

    if user_in_company(request.user, company):
        property_list = Property.objects.filter(real_estate_company=company)\
            .order_by('title')

        return render(request, "recontent/properties.html", 
            {'company':company, 'property_list':property_list})
    else:
        return render(request, "recontent/access_denied.html", 
            {'company':company})


def company_support(request, **kwargs):
    '''
    Eventually we'll have some sort of support system for business users
    '''
    slug = kwargs["slug"]
    company = Company.objects.get(slug=slug)

    if user_in_company(request.user, company):
        return render(request, "recontent/support.html", 
            {'company':company})
    else:
        return render(request, "recontent/access_denied.html", 
            {'company':company})


