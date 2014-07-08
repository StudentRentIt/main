
<<<<<<< HEAD

=======
>>>>>>> 953247464bbd149e315d738b8a76f7bf52aa9a66
class FormValidateMixin(object):

    def form_invalid(self, form, **kwargs):
        #need to add in the error status to the context_data
        context = self.get_context_data(**kwargs)
        context['status'] = 'error'
        context['form'] = form
        return self.render_to_response(context)

    def form_valid(self, form, **kwargs):
        #need to add in the saved status to the context_data
        context = self.get_context_data(**kwargs)
        context['status'] = 'saved'
        context['form'] = form

        form.instance.save()
        return self.render_to_response(context)