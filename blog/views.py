from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

from property.models import Property
from school.models import School
from blog.models import Article


def home(request):
    '''
    Show the home for general blogs
    '''
    template_name = "blogcontent/home.html"
    object_list = Article.objects.filter(active=True, general_page=True)[0:5]

    return render(request, template_name, {'object_list': object_list})


def article(request, **kwargs):
    #show individual blog articles
    template_name = "blogcontent/article.html"
    object = get_object_or_404(Article, id=kwargs['pk'])

    return render(request, template_name, {'object': object})


def type(request, **kwargs):
    #show all blog articles of a certain type (property, school, tag, etc)
    template_name = "blogcontent/type.html"
    type = kwargs['type']
    id = kwargs['pk']

    if type == "school":
        object = get_object_or_404(School, id=id)
        object_list = Article.objects.filter(school=id)
    elif type == "property":
        object = get_object_or_404(Property, id=id)
        object_list = Article.objects.filter(property=id)

    return render(request, template_name, {'object': object, 'object_list': object_list,
                                            'type': type})
