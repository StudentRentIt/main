from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView

from .models import Company
from .utils import user_in_company
from main.models import UserProfile
        

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
        agents = UserProfile.objects.filter(real_estate_company=company)
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
        members = UserProfile.objects.filter(real_estate_company=company)
        
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
                user.profile.real_estate_company = None
            elif request.POST["submit"] == "add":
                try:
                    username = request.POST["username"]
                    user = User.objects.get(username=username)
                    user.profile.real_estate_company = company
                except User.DoesNotExist:
                    context['error_msg'] = username + " does not exist"
                    return render(request, template_name, context)

            user.profile.save()

        return render(request, template_name, context)
    else:
        return render(request, 'recontent/access_denied.html', 
            {'company':company})


