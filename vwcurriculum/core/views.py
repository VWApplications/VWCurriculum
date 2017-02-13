from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Profile


class HomeView(View):
  template = 'core/home.html'

  def get(self, request):
    profile = Profile.objects.get(id=1)
    skills = filter_skills(request, profile.skills.all())
    skills = pagination(request, skills, 20)
    certificates = pagination(request, profile.certificates.all(), 5)
    projects = pagination(request, profile.projects.all(), 5)
    experiences = pagination(request, profile.experiences.all(), 5)
    context = {
      'skills': skills,
      'certificates': certificates,
      'projects': projects,
      'experiences': experiences,
    }
    return render(request, self.template, context)


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


def filter_skills(request, skills):
  category = request.GET.get('category', '')
  if category == 'Framework':
    return skills.filter(category=category)
  if category == 'Linguagens':
    return skills.filter(category=category)
  if category == 'Design':
    return skills.filter(category=category)
  if category == 'Devops':
    return skills.filter(category=category)
  if category == 'Governanca':
    return skills.filter(category='Governança de TI')
  if category == 'Outras':
    return skills.filter(category=category)
  return skills

