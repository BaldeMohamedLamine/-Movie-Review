from django.conf import settings
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LoginView
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.http import urlsafe_base64_decode
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import View

from .forms import CustomAuthenticationForm
from .forms import CustomUserCreationForm
from .forms import ProfileForm
from .models import Profile
from .utils.send_emails import send_activation_email
from users.models import User


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm

    def get_success_url(self):
        return reverse_lazy('film_list')


class CustomUserCreationView(CreateView):
    template_name = 'registration/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('register')

    def form_valid(self, form):
        with transaction.atomic():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            send_activation_email(user)
        messages.success(
            self.request,
            ("Votre compte compte a ete cree, consulter "
                "votre boite email pour activer votre compte")
        )
        return redirect(self.success_url)


class ActivationUserView(View):
    login_url = reverse_lazy('login')

    def get(self, request, uid, token):
        id = urlsafe_base64_decode(uid)
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return render(request, 'registration/activation_invalid.html')

        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(
                self.request,
                "Votre compte a ete active. Vous pouvez vous connecter "
            )
            return redirect(self.login_url)
        return render(request, 'registration/activation_invalid.html')



class LogoutView(View):
    login_url = reverse_lazy('login')

    def get(self, request):
        logout(request)
        messages.success(
            self.request,
            "Votre a ete deconnecte"
        )
        return redirect(self.login_url)

#por creer atomatiqmet le profil
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


def profile_view(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'registration/profile.html', {'form': form})
