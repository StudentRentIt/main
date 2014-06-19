from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse_lazy
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView

from braces.views import LoginRequiredMixin
from main.models import Property, PropertyImage, PropertyRoom, PropertyFavorite, \
    Service, Package, PropertyVideo, Article, Event, Roommate, Deal
from main.forms import BasicPropertyForm, DetailPropertyForm, ContactForm, \
    RoomPropertyForm, ContactPropertyForm, ImagePropertyForm, FavoriteForm, ReserveForm, \
    BusinessDetailPropertyForm, VideoPropertyForm, ScheduleForm
from main.utils import get_favorites, save_impression


class BusinessDetailView(DetailView):

    model = Property
    template_name = "propertycontent/business.html"

    def get(self, request, *args, **kwargs):
        '''
        override to save impression
        '''
        self.object = self.get_object()
        save_impression(imp_type="P", imp_property=self.object)
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        #get the property images
        context = super(BusinessDetailView, self).get_context_data(**kwargs)
        context['property_images'] = PropertyImage.objects.filter(property=self.object.id)
        return context


def property(request, pk, slug, action = None):
    '''
    displays the full listing for properties and functions such as contact owner,
    or set up a reservation. Need to gather the property information room/pictures, contactform,
    and reserveform.

    FBV because would need to redifine pretty much all of the post function in CBV
    to handle multiple form submission
    '''
    property = get_object_or_404(Property, id=pk)
    save_impression(imp_type="P", imp_property=property)

    #perform certain actions that are passed in in the action kwarg
    if action == "reserve":
        load_modal = "propertyReserveModal"
    elif action == "contact":
        load_modal = "propertyContactModal"
    elif action == "schedule":
        load_modal = "propertyScheduleModal"
    else:
        load_modal = slug

    property_images = PropertyImage.objects.filter(property=pk, floorplan=False)
    floorplan_images = PropertyImage.objects.filter(property=pk, floorplan=True)
    property_rooms = PropertyRoom.objects.filter(property=pk)
    property_videos = PropertyVideo.objects.filter(property=pk)

    favorited = get_favorites(request.user)
    template = 'propertycontent/property.html'
    base_dir = settings.BASE_DIR
    related_properties = property.get_related_properties()

    for p in related_properties:
        save_impression(imp_type="S", imp_property=p)

    #set form defaults if the user is logged in
    if request.user.is_authenticated():
        email = request.user.email
        first_name = request.user.first_name
        last_name = request.user.last_name
    else:
        email = None
        first_name = None
        last_name = None

    #shared initial values dictionary to be used on multiple forms
    initial_dict = {'first_name':first_name, 'last_name':last_name, 'email':email}

    #set contact forms to use
    contact_form = ContactForm()
    initial_contact_form = ContactForm(initial=initial_dict)

    #filter room choices and set the reserve forms
    room_choices = PropertyRoom.objects.filter(property=property.id)
    reserve_form = ReserveForm()
    reserve_form.fields["floor_plan"].queryset = room_choices
    initial_reserve_form = ReserveForm(initial=initial_dict)
    initial_reserve_form.fields["floor_plan"].queryset = room_choices

    #setup for the schedule form
    schedule_form = ScheduleForm()
    initial_schedule_form = ScheduleForm(initial=initial_dict)

    render_dict = {'property':property, 'property_images':property_images,
        'property_rooms':property_rooms, 'favorited':favorited, 'contact_form':contact_form,
        'reserve_form':reserve_form, 'floorplan_images':floorplan_images,
        'related_properties': related_properties, 'load_modal':load_modal,
        'schedule_form':schedule_form, 'property_videos':property_videos}

    if request.method == "POST":
        #only send to property contact if in production
        internal_email = 'support@studentrentit.com'
        if base_dir == "/home/studentrentit/prod":
            email_to = [property.contact_email]
            email_bcc = [internal_email]
        else:
            email_to = ['awwester@gmail.com']
            email_bcc = []

        if 'body' in request.POST:
            #handle if contact form was submitted
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                #handle if ContactForm was submitted
                cd = contact_form.cleaned_data
                body_footer = "<p>" + cd["first_name"] + " " + cd["last_name"] + " can be reached by email at " + cd['email'] + " or calling their phone at " + cd['phone_number'] + '.'
                headers = {'Reply-To': cd['email']}
                email_to.append(cd['email'])

                #build the email and send it
                msg = EmailMessage('StudentRentIt.com - Property Contact',
                                    get_template('email/default.html').render(
                                        Context({
                                            'body':cd['body'] + body_footer,
                                            'webURLroot' : settings.WEB_URL_ROOT,
                                            'email_header' : 'Property Contact from StudentRentIt.com'
                                        })
                                    ),
                                    settings.EMAIL_HOST_USER,
                                    email_to,
                                    headers=headers
                                  )
                msg.content_subtype = "html"  # Main content is now text/html
                msg.send()

                contact = contact_form.save(commit=False)
                contact.property = property
                contact.save()

                return render(request, template,
                    dict(render_dict, **{'contact_form':initial_contact_form, 'status':'sent'}))

            else:
                #contact_form errors
                return render(request, template,
                    dict(render_dict, **{'contact_form':contact_form, 'status':'error',
                            'load_modal':'propertyContactModal'}))
        elif 'floor_plan' in request.POST:
            #handle if ReserveForm was submitted and reset the rooms to the queryset in case of error
            reserve_form = ReserveForm(request.POST)
            reserve_form.fields["floor_plan"].queryset = room_choices
            if reserve_form.is_valid():
                #handle if ReserveForm was submitted
                reserve = reserve_form.save(commit=False)
                reserve.property = property
                #save the user if logged in
                try:
                    reserve.user = User.objects.get(username = request.user)
                except User.DoesNotExist:
                    pass
                reserve.save()

                cd = reserve_form.cleaned_data
                headers = {'Reply-To': cd['email']}
                body_footer = "<p>They can be reached by email at " + cd['email'] + " or calling their phone at " + cd['phone_number'] + '.'
                email_to.append(cd['email'])

                #build up body text
                body = cd["first_name"] + " " + cd["last_name"] + ' has filed a reservation' + \
                ' for ' + property.title + ' through StudentRentIt.com. They are interested in the ' + \
                str(cd['floor_plan']) + ' with an anticipated move in date of ' + \
                cd['move_in_date'].strftime('%b %d %Y') + '.'

                if cd['felony'] == "True":
                    body += ' They have a felony. '
                else:
                    body += ' They do not have a felony'

                if cd['evicted'] == "True":
                    body += ' They have been evicted before.'
                else:
                    body += ' They have not been evicted before.'

                if cd['credit'] == "True":
                    body += ' They have decent credit or a guarantor.'
                else:
                    body += ' They do not have decent credit nor a guarantor.'

                body += body_footer

                #build the email and send it
                msg = EmailMessage('StudentRentIt.com - Property Reservation',
                                    get_template('email/default.html').render(
                                        Context({
                                            'body' : body,
                                            'webURLroot' : settings.WEB_URL_ROOT,
                                            'email_header' : 'Property Reservation from StudentRentIt.com'
                                        })
                                    ),
                                    settings.EMAIL_HOST_USER,
                                    email_to,
                                    headers=headers
                                  )
                msg.content_subtype = "html"  # Main content is now text/html
                msg.send()

                return render(request, template,
                    dict(render_dict, **{'reserve_form':initial_reserve_form, 'status':'sent'}))
            else:
                #reserve_form errors
                return render(request, template,
                    dict(render_dict, **{'reserve_form':reserve_form, 'status':'error',
                            'load_modal':'propertyReserveModal'}))

        elif 'schedule_date' in request.POST:
            #handle if the schedule form was submitted
            schedule_form = ScheduleForm(request.POST)
            if schedule_form.is_valid():
                schedule = schedule_form.save(commit=False)
                schedule.property = property

                #save the user if logged in
                try:
                    schedule.user = User.objects.get(username = request.user)
                except User.DoesNotExist:
                    pass
                schedule.save()

                cd = schedule_form.cleaned_data
                headers = {'Reply-To': cd['email']}
                body_footer = "<p>They can be reached by email at " + cd['email'] + " or calling their phone at " + cd['phone_number'] + '.'
                email_to.append(cd['email'])

                #build up body text
                body = cd["first_name"] + " " + cd["last_name"] + ' has scheduled a tour on ' + cd['schedule_date'].strftime('%b %d %Y') + \
                    ' at ' + cd['schedule_time'].strftime('%I:%M %p') + '. Please follow up with them to confirm or change the appointment.'\
                    + body_footer

                #build the email and send it
                msg = EmailMessage('StudentRentIt.com - Apartment Tour',
                                    get_template('email/default.html').render(
                                        Context({
                                            'body' : body,
                                            'webURLroot' : settings.WEB_URL_ROOT,
                                            'email_header' : 'Tour Scheduled from StudentRentIt.com'
                                        })
                                    ),
                                    settings.EMAIL_HOST_USER,
                                    email_to,
                                    email_bcc,
                                    headers=headers
                                  )
                msg.content_subtype = "html"  # Main content is now text/html
                msg.send()

                return render(request, template,
                    dict(render_dict, **{'schedule_form':initial_schedule_form, 'status':'sent'}))
            else:
                #schedule_form errors
                return render(request, template,
                    dict(render_dict, **{'schedule_form':schedule_form, 'status':'error',
                            'load_modal':'propertyScheduleModal'}))

    return render(request, template,
        dict(render_dict, **{'reserve_form':initial_reserve_form,
            'contact_form':initial_contact_form, 'schedule_form':initial_schedule_form}))


class ManagePropertyTemplateView(LoginRequiredMixin, TemplateView):
    '''
    shows the options for what you can manage
    '''

    template_name = 'propertycontent/manage.html'


class PropertyCreateView(LoginRequiredMixin, CreateView):
    '''
    create the required fields on a property model instance
    '''

    model = Property
    form_class = BasicPropertyForm
    template_name = 'propertycontent/add.html'

    def get_context_data(self, **kwargs):
        #set some static context variables to pass into panel form
        context = super(PropertyCreateView, self).get_context_data(**kwargs)
        context['form_submit_text'] = "Continue"
        context['form_title_text'] = "First, let's get the basics"
        return context

    def form_valid(self, form, **kwargs):
        #save the user to the instance
        form.instance.user = self.request.user
        form.instance.save()

        context = self.get_context_data(**kwargs)
        context['status'] = 'saved'
        context['form'] = form
        return super(PropertyCreateView, self).form_valid(form)

    def get_success_url(self):
        #redirect to the newly created object
        return reverse_lazy('update-property', kwargs={'pk':self.object.id})


@login_required
def updateproperty(request, pk=None, type=None, type_id=None, function=None):
    '''
    allows users to manage their listings which can be roommate listing or property
    '''
    update_template = 'propertycontent/update.html'

    if pk:
        '''
        id provided means that the user is ready to edit a specific property

        module variables that will be used in multiple occasions
        '''
        property = get_object_or_404(Property, id=pk, user=request.user)
        rooms = PropertyRoom.objects.filter(property=property)
        images = PropertyImage.objects.filter(property=property)
        videos = PropertyVideo.objects.filter(property=property)

        #get corresponding type instance
        if type == "room" and type_id:
            room = get_object_or_404(PropertyRoom, id=type_id)
        if type == "video" and type_id:
            video = get_object_or_404(PropertyVideo, id=type_id)
        elif type == "image" and type_id:
            image = get_object_or_404(PropertyImage, id=type_id)

        basic_form_btn_text = 'Save'
        show_room_form = False
        show_image_form = False
        show_video_form = False

        #form initials
        basic_form = BasicPropertyForm(instance=property)
        contact_form = ContactPropertyForm(instance=property)
        room_form = RoomPropertyForm()
        image_form = ImagePropertyForm()
        video_form = VideoPropertyForm()

        #business detail form excludes some extra fields from the normal detail
        if property.type == "BUS":
            detail_form = BusinessDetailPropertyForm(instance=property)
        else:
            detail_form = DetailPropertyForm(instance=property)

        #will be passed into the render always
        render_dict = {'basic_form_btn_text':basic_form_btn_text,'basic_form':basic_form,
                      'detail_form':detail_form, 'contact_form':contact_form,
                      'room_form':room_form, 'video_form':video_form, 'image_form':image_form,
                      'rooms':rooms, 'videos':videos, 'images':images, 'property':property}

        if request.method == "POST":
            '''
            This is a pretty girthy POST block. Essentially we're going to check to
            see which form was saved. We then will update that specific form, and
            then need to go back to the same page and do the initial loads of
            all the update forms
            '''
            #TODO: create function in utils.py to handle these duplicated blocks
            #update basic info
            if 'title' in request.POST:
                basic_form = BasicPropertyForm(request.POST, instance=property)

                if basic_form.is_valid():
                    basic_form.save()
                    return render(request, update_template,
                        dict(render_dict, **{'basic_form':basic_form, 'status':'saved'}))
                else:
                    #form is not valid
                    return render(request, update_template,
                        dict(render_dict, **{'basic_form':basic_form, 'status':'error'}))

            #update detail info
            if 'special' in request.POST:
                if property.type == "BUS":
                    detail_form = BusinessDetailPropertyForm(request.POST, instance=property)
                else:
                    detail_form = DetailPropertyForm(request.POST, instance=property)

                if detail_form.is_valid():
                    detail_form.save()
                    return render(request, update_template,
                        dict(render_dict, **{'detail_form':detail_form, 'status':'saved',
                            'active_tab':'details'}))
                else:
                    #form is not valid
                    return render(request, update_template,
                        dict(render_dict, **{'detail_form':detail_form, 'status':'error',
                            'active_tab':'details'}))
            #update contact info
            if 'contact_first_name' in request.POST:
                contact_form = ContactPropertyForm(request.POST, instance=property)

                if contact_form.is_valid():
                    contact_form.save()
                    return render(request, update_template,
                        dict(render_dict, **{'contact_form':contact_form, 'status':'saved',
                            'active_tab':'contact'}))
                else:
                    #form is not valid
                    return render(request, update_template,
                        dict(render_dict, **{'contact_form':contact_form, 'status':'error',
                            'active_tab':'contact'}))
            #update room info
            if 'price' in request.POST:
                #determines whether update or create
                try:
                    room_form = RoomPropertyForm(request.POST, instance=room)
                except UnboundLocalError:
                    room_form = RoomPropertyForm(request.POST)

                if room_form.is_valid():
                    #set property FK
                    room = room_form.save(commit=False)
                    room.property = property
                    room.save()
                    return render(request, update_template,
                        dict(render_dict, **{'room_form':room_form, 'status':'saved',
                            'active_tab':'rooms'}))
                else:
                    #form is not valid
                    return render(request, update_template,
                        dict(render_dict, **{'room_form':room_form, 'status':'error',
                            'active_tab':'rooms', 'show_room_form':True}))
            #update pictures
            if 'caption' in request.POST:
                #determines whether update or create
                try:
                    image_form = ImagePropertyForm(request.POST, request.FILES, instance=image)
                except UnboundLocalError:
                    image_form = ImagePropertyForm(request.POST, request.FILES)

                if image_form.is_valid():
                    #set property FK
                    image = image_form.save(commit=False)
                    image.property = property
                    image.save()
                    return render(request, update_template,
                        dict(render_dict, **{'image_form':image_form, 'status':'saved',
                            'active_tab':'pics'}))
                else:
                    #form is not valid
                    return render(request, update_template,
                        dict(render_dict, **{'image_form':image_form, 'status':'error',
                            'active_tab':'pics', 'show_image_form':True}))
            #update videos
            if 'video_link' in request.POST:
                #determines whether update or create
                try:
                    video_form = VideoPropertyForm(request.POST, request.FILES, instance=video)
                except UnboundLocalError:
                    video_form = VideoPropertyForm(request.POST, request.FILES)

                if video_form.is_valid():
                    #set property FK
                    video = video_form.save(commit=False)
                    video.property = property
                    video.save()
                    return render(request, update_template,
                        dict(render_dict, **{'video_form':video_form, 'status':'saved',
                            'active_tab':'videos'}))
                else:
                    #form is not valid
                    return render(request, update_template,
                        dict(render_dict, **{'video_form':video_form, 'status':'error',
                            'active_tab':'videos', 'show_video_form':True}))

        else:
            #request.method not POST
            active_tab = "basic"

            if type == "addroom":
                #add new room chosen
                show_room_form = True
                active_tab = "rooms"

                return render(request, update_template,
                    dict(render_dict, **{'show_room_form':show_room_form, 'active_tab':active_tab}))

            if type == "addimage":
                #add new room chosen
                show_image_form = True
                active_tab = "pics"

                return render(request, update_template,
                    dict(render_dict, **{'show_image_form':show_image_form, 'active_tab':active_tab}))

            if type == "addvideo":
                #add new video chosen
                show_video_form = True
                active_tab = "videos"

                return render(request, update_template,
                    dict(render_dict, **{'show_video_form':show_video_form, 'active_tab':active_tab}))

            #looking at a room instance
            if type == "room" and type_id:
                active_tab = "rooms"

                if function == "delete":
                    #delete the selected room if the property user is request.user
                    if room.property.user == request.user:
                        room.delete()
                else:
                    room_form = RoomPropertyForm(instance=room)
                    show_room_form = True

            #looking at a image instance
            if type == "image" and type_id:
                active_tab = "pics"

                if function == "delete":
                    #delete the selected image if the property user is request.user
                    if image.property.user == request.user:
                        image.delete()
                else:
                    image_form = ImagePropertyForm(instance=image)
                    show_image_form = True

            #looking at a video instance
            if type == "video" and type_id:
                active_tab = "videos"

                if function == "delete":
                    #delete the selected video if the property user is request.user
                    if video.property.user == request.user:
                        video.delete()
                else:
                    video_form = VideoPropertyForm(instance=video)
                    show_video_form = True

            return render(request, update_template,
                dict(render_dict, **{'image_form':image_form, 'video_form':video_form,
                    'active_tab':active_tab, 'show_room_form':show_room_form, 'show_video_form':show_video_form,
                    'show_image_form':show_image_form, 'room_form':room_form}))
    else:
        #when the id is not provided, user picks one of their properties to edit
        user_properties = Property.objects.filter(user=request.user.id)

        return render(request, update_template,
                {'properties':user_properties, 'status':'choose'})


@login_required
def favorites(request, id=None):
    '''
    shows the favorites page
    '''
    favorites = PropertyFavorite.objects.filter(user=request.user)
    properties = Property.objects.all()
    favorited = get_favorites(request.user)

    for f in favorites:
        save_impression(imp_type="F", imp_property=f.property)

    render_dict = {'favorites':favorites, 'properties':properties,
        'favorited':favorited}

    if id:
        favorite = get_object_or_404(PropertyFavorite, id=id)
        if request.method == "POST":
            form = FavoriteForm(request.POST, instance=favorite)
            if form.is_valid():
                form.save()
                return render(request, 'maincontent/favorites.html',
                    dict(render_dict, **{'status':'saved'}))
            else:
                #form not valid
                return render(request, 'maincontent/favorites.html',
                    dict(render_dict, **{'form':form}))
        else:
            form = FavoriteForm(initial = {'property':favorite.property,
                                            'user':favorite.user,
                                            'note':favorite.note})
        return render(request, 'maincontent/favorites.html',
            dict(render_dict, **{'form':form, 'favorite':favorite}))

    return render(request, 'maincontent/favorites.html',
        render_dict)


def favorite(request, action=None):
    '''
    passed in as a json object to add a favorite for a user
    '''
    if request.user.is_authenticated():
        if request.is_ajax():
            if request.method == 'POST':
                property_id = request.POST['property_id'].replace('favorite', '')
                property = get_object_or_404(Property, id=property_id)
                user = request.user

                if action == "add":
                    #save favorite if doesn't already exist for the user
                    try:
                        PropertyFavorite.objects.get(user=user, property=property)
                        return HttpResponse("user/favorite combo already exists")
                    except:
                        favorite = PropertyFavorite()
                        favorite.property = property
                        favorite.user = user
                        favorite.save()
                        return HttpResponse("save successful")
                elif action == "remove":
                    if request.method == "POST":
                        try:
                            favorite = get_object_or_404(PropertyFavorite, property=property, user=user)
                            favorite.delete()
                            return HttpResponse("deleted successfully")
                        except Exception as e:
                            return HttpResponse("error during deletion: " + e)
                else:
                    return HttpResponse("unrecognized action")
    else:
        return HttpResponse("User Not Logged In")

'''
the following 2 payment functions aren't currently used, and I have a feeling we will
be getting rid of them. AWW 20140606
'''
@login_required
def recurring_services(request, **kwargs):
    '''
    Used for packages and recurring services. These are services that are provided
    each month either on the website or outside of the website. Pcakages are essentially
    a grouping of recurring services.
    '''
    monthly_services = Service.objects.filter(service_type="R", active=True)
    packages = Package.objects.all()
    property = get_object_or_404(Property, id=kwargs['pk'], user=request.user)

    previous_property_package = property.package
    fill_package = previous_property_package

    #added for debugging, can remove after i think and remove from render dict
    current_services = property.services.all()
    added_services = []
    removed_services = []
    future_services = ""

    if request.method == "POST":
        '''
        When they post a change to their packages or services we will want to update
        their property model as well as insert a into the PropertyChange and/or ServiceChange
        tables. We will want to send an email to ourselves as well as the property with
        the change info. We will want to see what the old packages and services were
        as well as the future packages and services.

        We will get the service and package changes and then email the property owner.
        In the future we will automate these changes and payment
        '''
        future_property_package = None

        #get which packages and services should be saved to the property
        if request.POST["package"]:
            future_property_package = get_object_or_404(Package, id=request.POST["package"])
            fill_package = future_property_package

            #save the package to the property
            if future_property_package != "":
                property.package = future_property_package
                property.save()
        elif previous_property_package and not request.POST["package"]:
            #if there was not a previous package and now there's not, remove.
            property.package = None
            property.save()
            '''
            need to know what the previous package was to send an email or not,
            but also don't want the hidden input to fill with the id. Set a variable
            to not fill the value of the hidden input
            '''
            #fill_package_input = False

        '''
        if future services are not in the current services add it to the property
        services. If the future services has items that aren't in the current services
        remove them from the property services.
        '''
        future_services_string = request.POST["services"]
        if future_services_string:
            future_services_list = future_services_string.split(", ")
            future_services = Service.objects.filter(id__in=future_services_list)

            for i in future_services:
                if i not in current_services and i.service_type == "R":
                    added_services.append(i)

            if current_services != '':
                for i in current_services:
                    if i not in future_services:
                        removed_services.append(i)
        else:
            # if there are no future services, remove the current services
            if current_services:
                removed_services = current_services


        #perform db actions to save or remove services
        for s in removed_services:
            s.delete()
            s.save()

        for s in added_services:
            property.services.add(s)
            property.save()

        #determine whether we should send an email or not
        send_email = False

        if added_services or removed_services or previous_property_package != future_property_package:
            send_email = True

        if send_email:
            #generate email
            #only send to property contact if in production
            if settings.BASE_DIR == "/home/studentrentit/prod":
                email_to = [property.contact_email, 'support@studentrentit.com']
            else:
                email_to = ['awwester@gmail.com']

            #build the email and send it
            package_change = ""
            recurring_service_change = ""

            if previous_property_package != future_property_package:
                package_change = "<h3 class='text-center'>Package Changes</h3>"
                if property.package:
                    package_change += "<p>Your new package will be the " + property.package.title + ' package</p>'
                else:
                    package_change += "You have removed your package."

            if added_services or removed_services:
                recurring_service_change = "<h3  class='text-center'>Recurring Service Changes</h3>"
                if added_services:
                    added_service_string = ""
                    for a in added_services:
                        if added_service_string:
                            added_service_string += ', ' + a.title
                        else:
                            added_service_string = a.title
                    recurring_service_change += "<p>You have added the following recurring services: " + added_service_string

                if removed_services:
                    removed_service_string = ""
                    for r in removed_services:
                        if removed_service_string:
                            removed_service_string += ', ' + r.title
                        else:
                            removed_service_string = r.title
                    recurring_service_change += "<p>You have removed the following recurring services: " + removed_service_string

                current_services = property.services.all()
                if current_services:
                    current_service_string = ""
                    for s in current_services:
                        if current_service_string:
                            current_service_string += ', ' + s.title
                        else:
                            current_service_string = s.title
                    recurring_service_change += "<p>Your new current services are: " + current_service_string

            body = "<p>This email is informing you of your recent change to your services. We will " + \
            "be following up with you shortly.</p>" + package_change + recurring_service_change
            # + onetime_service_purchase

            msg = EmailMessage('StudentRentIt.com - Property Service Change',
                                get_template('email/default.html').render(
                                    Context({
                                        'body':body,
                                        'webURLroot' : settings.WEB_URL_ROOT,
                                        'email_header' : 'Service Change at StudentRentIt.com'
                                    })
                                ),
                                settings.EMAIL_HOST_USER,
                                email_to
                              )
            msg.content_subtype = "html"  # Main content is now text/html
            msg.send()

    return render(request, 'propertycontent/recurring_services.html',
        {'monthly_services':monthly_services, 'onetime_services':onetime_services,
        'packages':packages, 'property':property, 'fill_package':fill_package})
        #'previous_property_package':fill_


def onetime_services(request, **kwargs):
    '''
    used to accept onetime service payments. These payments are services that are
    applied and charged to a property. They can be either website based such as
    website sponsorship, or can be a service that is provided outside of the website
    such as video creation or email blast.
    '''
    property = get_object_or_404(Property, id=kwargs['pk'], user=request.user)
    onetime_services = Service.objects.filter(service_type="O", active=True)
    public_key = settings.STRIPE_PUBLIC_KEY

    return render(request, 'propertycontent/onetime_services.html',
        {'onetime_services':onetime_services, 'property':property, 'public_key':public_key})


def community(request, **kwargs):
    '''
    Used to show the community objects (article, event, deals, etc )for a property
    '''
    template_name = 'propertycontent/community.html'
    property = get_object_or_404(Property, id=kwargs['pk'])

    articles = Article.objects.filter(property=property)
    events = Event.objects.filter(property=property)
    roommates = Roommate.objects.filter(property=property)
    deals = Deal.objects.filter(property=property)

    return render(request, template_name, {'property':property,
        'articles':articles, 'events':events, 'roommates':roommates, 'deals':deals})

'''
Removing these 2 Property Article views and replacing with the blog app.
AWW 20140606

class PropertyArticleListView(ListView):

    template_name = "maincontent/blog/all.html"

    def get_context_data(self, **kwargs):
        #set some static context variables to pass into panel form
        context = super(PropertyArticleListView, self).get_context_data(**kwargs)
        context['property'] = get_object_or_404(Property, id=self.kwargs['pk'])
        return context

    def get_queryset(self):
        property_id = self.kwargs['pk']
        qs = Article.objects.filter(property=property_id)
        return qs


class PropertyArticleDetailView(DetailView):

    model = Article
    template_name = 'maincontent/blog/article.html'

    def get_object(self):
        pk = self.kwargs['pk']
        qs = get_object_or_404(Article, id=pk)
        return qs

    def get_context_data(self, **kwargs):
        #set some static context variables to pass into panel form
        context = super(PropertyArticleDetailView, self).get_context_data(**kwargs)
        property = get_object_or_404(Property, id=self.kwargs['property_pk'])
        context['property'] = property
        object_id = get_object_or_404(Article, id=kwargs['object'].id).id
        previous_article = Article.objects.filter(property=property, id__lt=object_id)
        next_article = Article.objects.filter(property=property, id__gt=object_id)

        try:
            context['author'] = TeamMember.objects.get(user=kwargs['object'].user)
        except:
            pass

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