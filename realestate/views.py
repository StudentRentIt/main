from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import UpdateView
from django.views.generic.detail import SingleObjectMixin

from .models import Company
from .forms import CompanyForm
from .utils import user_in_company
from property.models import Property
        

class CompanyAccessMixin(object):
    '''
    check if a user is in a certain company. If they are, let them
    see the view. If they're not, send them to the access_denied
    '''
    def dispatch(self, request, *args, **kwargs):
        company = self.get_object()
 
        if not user_in_company(self.request.user, company):
            return render(request, 'recontent/access_denied.html', 
                {'company':company})
        else:
            return super(CompanyAccessMixin, self).dispatch(
                request, *args, **kwargs)


class HomeTemplateView(TemplateView):
    '''
    This will be information for real estate companies that might want 
    to join us.
    '''
    template_name = 'recontent/home.html'


class CompanyHomeFormView(CompanyAccessMixin, UpdateView):
    template_name = 'recontent/company_home.html'
    model = Company
    form_class = CompanyForm

    def get_context_data(self, **kwargs):
        context = super(CompanyHomeFormView, self).get_context_data(**kwargs)
        context['agents'] = get_user_model().objects.filter(real_estate_company=self.object)
        context['page'] = 'home'
        return context


class CompanyPropertiesListView(CompanyAccessMixin, DetailView):
    template_name = "recontent/properties.html"
    model = Company

    def get_context_data(self, **kwargs):
        context = super(CompanyPropertiesListView, self).get_context_data(**kwargs)
        context['property_list'] = Property.objects.filter(real_estate_company=self.get_object())
        return context


class CompanySupportTemplateView(CompanyAccessMixin, DetailView):
    template_name = "recontent/support.html"
    model = Company


@login_required
def company_members(request, **kwargs):
    '''
    place for real estate companies to manage their members
    TODO: Convert this into a CBV
    '''
    slug = kwargs["slug"]
    company = Company.objects.get(slug=slug)

    if user_in_company(request.user, company):
        template_name = 'recontent/members.html'
        page = "members"

        members = get_user_model().objects.filter(real_estate_company=company)
        
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
                user = get_user_model().objects.get(id=user_id)
                user.real_estate_company = None
            elif request.POST["submit"] == "add":
                try:
                    username = request.POST["username"]
                    user = get_user_model().objects.get(username=username)
                    user.real_estate_company = company
                except get_user_model().DoesNotExist:
                    context['error_msg'] = username + " does not exist"
                    return render(request, template_name, context)

            user.save()

        return render(request, template_name, context)
    else:
        return render(request, 'recontent/access_denied.html', 
            {'company':company})


