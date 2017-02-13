from .models import Profile


def profile(request):
  context = {
    'profile': Profile.objects.get(id=1)
  }
  return context
