from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import Profile, Skill


class HomeView(View):
  template = 'core/home.html'

  def get(self, request):
    skills = Skill.objects.all()
    skills = pagination(request, skills, 20)
    context = {
      'profile': Profile.objects.get(id=1),
      'skills': skills,
    }
    return render(request, self.template, context)


def search_certificates(request, certificates):
  query = request.GET.get("q_certificate")
  if query:
    certificates = certificates.filter(
                    Q(title__icontains=query) |
                    Q(content__icontains=query)
                   ).distinct()
  return certificates


def pagination(request, object_list, amount):
  paginator = Paginator(object_list, amount)
  page = request.GET.get('page')
  try:
    objects = paginator.page(page)
  except PageNotAnInteger:
    objects = paginator.page(1)
  except EmptyPage:
    objects = paginator.page(paginator.num_pages)
  return objects
