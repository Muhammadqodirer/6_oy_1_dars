TIME_ZONE = 'Asia/Tashkent'

USE_TZ = True

LANGUAGE_CODE = 'uz'

MIDDLEWARE = [
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.timezone.TimezoneMiddleware'
]

from django.shortcuts import render
from django.utils import timezone
from django.utils.translation import gettext as _

def home(request):
    current_time = timezone.now()
    message = _("Assalomu aleykum asadbek sobirov")
    return render(request, 'home.html', {'current_time': current_time, 'message': message})