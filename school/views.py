from django.shortcuts import get_object_or_404
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic import ListView, RedirectView
from django.core.urlresolvers import reverse_lazy, reverse

from main.views import FormValidateMixin
from main.utils import save_impression

from school.models import School, Roommate, Deal, Event
from school.forms import RoommateForm, EventForm, DealForm

from blog.models import Article
from blog.forms import ArticleForm

from property.models import Property

from braces.views import LoginRequiredMixin


class SchoolRedirectView(RedirectView):

    def get_redirect_url(self, pk, slug):
        #pass the arguments and default redirect to articles
        return reverse('school-articles', args=(pk, slug, 'articles'))


'''*****************************************************************
                School Create Update Section
This section has the logic for creating school models and displaying
their respective templates.
'''

class SchoolCreateView(CreateView): #loginrequiredmixin removed
    '''
    shared view class for the school create views
    '''

    def get(self, request, *args, **kwargs):
        '''
        run extra code to save the impression on get
        '''
        self.object = None
        properties = Property.objects.filter(sponsored=True, school=self.kwargs['pk'])
        for p in properties:
            save_impression(imp_type="B", imp_property=p)

        return super(SchoolCreateView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SchoolCreateView, self).get_context_data(**kwargs)
        context['school'] = get_object_or_404(School, id=self.kwargs['pk'])
        context['articles'] = Article.objects.filter(school=self.kwargs['pk'], general_page=False)
        context['events'] = Event.objects.filter(school=self.kwargs['pk'])
        context['deals'] = Deal.objects.filter(school=self.kwargs['pk'])
        context['roommates'] = Roommate.objects.filter(school=self.kwargs['pk'])
        context['sponsored_properties'] = Property.objects.filter(sponsored=True, school=self.kwargs['pk'])
        context['page'] = self.kwargs['type']
        return context

    #TODO: form validation should be defined at a lower-level such as ProcessFormView
    def form_invalid(self, form, **kwargs):
        #need to add in the error status to the context_data
        context = self.get_context_data(**kwargs)
        context['status'] = 'error'
        context['form'] = form
        return self.render_to_response(context)

    def form_valid(self, form, **kwargs):
        ''''
        need to add in the saved status to the context_data
        add save to user and school before committing
        '''
        form.instance.user = self.request.user
        form.instance.school = get_object_or_404(School, id=self.kwargs['pk'])
        form.instance.save()

        context = self.get_context_data(**kwargs)
        context['status'] = 'saved'
        context['form'] = form
        return self.render_to_response(context)


class SchoolArticleCreateView(SchoolCreateView):

    template_name = 'schoolcontent/articles.html'
    form_class = ArticleForm

    def get_queryset(self):
        queryset = self.context['articles']
        return queryset


class SchoolEventCreateView(SchoolCreateView):

    template_name = 'schoolcontent/events.html'
    form_class = EventForm

    def get_queryset(self):
        queryset = self.context['events']
        return queryset


class SchoolDealCreateView(SchoolCreateView):

    template_name = 'schoolcontent/deals.html'
    form_class = DealForm

    def get_queryset(self):
        queryset = self.context['deals']
        return queryset


class SchoolRoommateCreateView(SchoolCreateView):

    template_name = 'schoolcontent/roommates.html'
    form_class = RoommateForm

    def get_queryset(self):
        queryset = self.context['roommates']
        return queryset



'''*****************************************************************
                School Info Update Section
This section has the logic for updating school models and displaying
their respective templates.
'''

class SchoolUpdateListView(LoginRequiredMixin, ListView):
    '''
    class to store the template_name variable and loginrequired, and maybe other
    things that pop up needed by the School ListViews
    '''
    template_name = 'schoolcontent/update/choose.html'

# the following UpdateListViews show users what they are able to update
class ArticleUpdateListView(SchoolUpdateListView):

    def get_queryset(self):
        qs = Article.objects.filter(user=self.request.user)
        return qs

class EventUpdateListView(SchoolUpdateListView):

    def get_queryset(self):
        qs = Event.objects.filter(user=self.request.user)
        return qs

class DealUpdateListView(SchoolUpdateListView):

    def get_queryset(self):
        qs = Deal.objects.filter(user=self.request.user)
        return qs

class RoommateUpdateListView(SchoolUpdateListView):

    def get_queryset(self):
        qs = Roommate.objects.filter(user=self.request.user)
        return qs


# the following UpdateViews do the work while updating school objects
class SchoolUpdateFormBaseView(LoginRequiredMixin, FormValidateMixin, UpdateView):
    '''
    creates a base class with mixins for the School Update Forms to inherit
    '''


class EventUpdateView(SchoolUpdateFormBaseView):

    model = Event
    form_class = EventForm
    template_name = 'schoolcontent/update/event.html'

    def get_context_data(self, **kwargs):
        #set some static context variables to pass into panel form
        context = super(EventUpdateView, self).get_context_data(**kwargs)
        context['header_text'] = "Which event do you want to update?"
        context['form_title_text'] = "Update Event"
        context['object_list'] = Event.objects.filter(user=self.request.user)
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('update-event', kwargs={'pk':self.kwargs['pk']})


class RoommateUpdateView(SchoolUpdateFormBaseView):

    model = Roommate
    form_class = RoommateForm
    template_name = 'schoolcontent/update/roommate.html'

    def get_context_data(self, **kwargs):
        #set some static context variables to pass into panel form
        context = super(RoommateUpdateView, self).get_context_data(**kwargs)
        context['header_text'] = "Which roommate posting do you want to update?"
        context['form_title_text'] = "Update Roommate Posting"
        context['object_list'] = Roommate.objects.filter(user=self.request.user)
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('update-roommate', kwargs={'pk':self.kwargs['pk']})


class DealUpdateView(SchoolUpdateFormBaseView):

    model = Deal
    form_class = DealForm
    template_name = 'schoolcontent/update/deal.html'

    def get_context_data(self, **kwargs):
        #set some static context variables to pass into panel form
        context = super(DealUpdateView, self).get_context_data(**kwargs)
        context['header_text'] = "Which deal do you want to update?"
        context['form_title_text'] = "Update Deal"
        context['object_list'] = Deal.objects.filter(user=self.request.user)
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('update-deal', kwargs={'pk':self.kwargs['pk']})


class ArticleUpdateView(SchoolUpdateFormBaseView):

    model = Article
    form_class = ArticleForm
    template_name = 'schoolcontent/update/article.html'

    def get_context_data(self, **kwargs):
        #set some static context variables to pass into panel form
        context = super(ArticleUpdateView, self).get_context_data(**kwargs)
        context['header_text'] = "Which article do you want to update?"
        context['form_title_text'] = "Update Article"
        context['object_list'] = Article.objects.filter(user=self.request.user)
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('update-article', kwargs={'pk':self.kwargs['pk']})



'''
Removing these 2 School Article views and replacing with the blog app.
AWW 20140606

class SchoolArticleListView(ListView):

    template_name = "maincontent/blog/all.html"

    def get_context_data(self, **kwargs):
        #set some static context variables to pass into panel form
        context = super(SchoolArticleListView, self).get_context_data(**kwargs)
        context['school'] = get_object_or_404(School, id=self.kwargs['pk'])
        return context

    def get_queryset(self):
        school_id = self.kwargs['pk']
        qs = Article.objects.filter(school=school_id)
        return qs

class SchoolArticleDetailView(DetailView):

    model = Article
    template_name = 'maincontent/blog/article.html'

    def get_object(self):
        pk = self.kwargs['pk']
        qs = get_object_or_404(Article, id=pk)
        return qs

    def get_context_data(self, **kwargs):
        #set some static context variables to pass into panel form
        context = super(SchoolArticleDetailView, self).get_context_data(**kwargs)
        school = get_object_or_404(School, id=self.kwargs['school_pk'])
        object_id = get_object_or_404(Article, id=kwargs['object'].id).id
        previous_article = Article.objects.filter(school=school, id__lt=object_id)
        next_article = Article.objects.filter(school=school, id__gt=object_id)
        context['school'] = school

        try:
            previous_id = previous_article[0].id
            context['previous_article'] = get_object_or_404(Article, id=previous_id)
        except:
            context['previous_article'] = None

        try:
            next_id = next_article.reverse()[0].id
            context['next_article'] = get_object_or_404(Article, id=next_id)
        except:
            context['next_article'] = None

        return context
'''