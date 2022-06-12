from django.views.generic import ListView

from .forms import ContactUsModelForm
from django.views.generic.edit import CreateView

from .models import UserProfile
from site_module.models import SiteSetting


class ContactUsView(CreateView):
    form_class = ContactUsModelForm
    template_name = 'contact_module/contact_us_page.html'
    success_url = '/contact-us/'

    def get_context_data(self, **kwargs):
        context = super(ContactUsView, self).get_context_data(**kwargs)
        current_settings: SiteSetting = SiteSetting.objects.filter(is_main_setting=True, ).first()
        context['setting'] = current_settings
        return context


def store_file(file):
    with open('temp/image.jpg', "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)


class CreateProfileView(CreateView):
    template_name = 'contact_module/create_profile_page.html'
    model = UserProfile
    fields = '__all__'
    success_url = '/contact-us/create-profile'


class ProfilesView(ListView):
    model = UserProfile
    template_name = 'contact_module/profiles_list_page.html'
    context_object_name = 'profiles'
