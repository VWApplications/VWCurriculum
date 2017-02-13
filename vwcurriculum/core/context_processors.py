from .models import Profile


def profile(request):
  context = {
    'profile': Profile.objects.get(first_name="Victor Hugo", last_name="Arnaud Deon")
  }
  return context
