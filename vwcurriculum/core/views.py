from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib import messages
from .models import Profile
from .forms import ContactForm


def home(request):
  template = 'core/home.html'
  profile = Profile.objects.get(id=1)
  context = {
    'skills': get_skills(request, profile),
    'certificates': get_certificates(request, profile),
    'projects': get_projects(request, profile),
    'experiences': get_experiences(request, profile),
  }
  form = ContactForm(request.POST or None)
  if form.is_valid():
    form.send_message()
    form = ContactForm()
    messages.success(request, "Seu email foi enviado com sucesso")
  else:
    form = ContactForm()
  context['form'] = form
  return render(request, template, context)


def get_skills(request, profile):
  skills = filter_skills(request, profile.skills.all())
  skills = pagination(request, skills, 20)
  return skills


def get_certificates(request, profile):
  certificates = filter_certificates(request, profile.certificates.all())
  certificates = search_certificate(request, certificates)
  certificates = pagination(request, certificates, 5)
  return certificates


def get_projects(request, profile):
  projects = search_project(request, profile.projects.all())
  projects = pagination(request, projects, 5)
  return projects


def get_experiences(request, profile):
  experiences = search_experience(request, profile.experiences.all())
  experiences = pagination(request, experiences, 5)
  return experiences


def search_certificate(request, certificates):
  query = request.GET.get("q_certificate")
  if query:
    certificates = certificates.filter(
                  Q(title__icontains=query) |
                  Q(issuing_institution__icontains=query)
                ).distinct()
  return certificates


def search_project(request, projects):
  query = request.GET.get("q_project")
  if query:
    projects = projects.filter(
                  Q(title__icontains=query) |
                  Q(institution__icontains=query)
                ).distinct()
  return projects


def search_experience(request, experiences):
  query = request.GET.get("q_experience")
  if query:
    experiences = experiences.filter(
                  Q(title__icontains=query) |
                  Q(short_title__icontains=query)
                ).distinct()
  return experiences


def filter_skills(request, skills):
  category = request.GET.get('skill_category', '')
  skills = filter_category(category, skills)
  return skills


def filter_certificates(request, certificates):
  category = request.GET.get('certificate_category', '')
  certificates = filter_category(category, certificates)
  return certificates


def filter_category(category, objects):
  if category == 'Framework':
    return objects.filter(category=category)
  if category == 'Linguagens':
    return objects.filter(category=category)
  if category == 'Design':
    return objects.filter(category=category)
  if category == 'Devops':
    return objects.filter(category=category)
  if category == 'Governanca':
    return objects.filter(category='Governança de TI')
  if category == 'Outras':
    return objects.filter(category=category)
  return objects


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
