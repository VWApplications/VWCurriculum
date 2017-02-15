from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib import messages
from .models import Profile
from .forms import ContactForm


def home(request):
  template = 'core/home.html'
  profile = Profile.objects.all()[0]
  context = {
    'profile': profile,
    'skills': get_skills(request, profile),
    'certificates': get_certificates(request, profile),
    'projects': get_projects(request, profile),
    'experiences': get_experiences(request, profile),
  }
  send_email(request, context)
  return render(request, template, context)


def send_email(request, context):
  form = ContactForm(request.POST or None)
  if form.is_valid():
    form.send_message()
    messages.success(request, "Seu email foi enviado com sucesso")
  context['form'] = form


def get_skills(request, profile):
  skills = filter_category(request, profile.skills.all(), 'skill_category')
  skills = pagination(request, skills, 20, 'skill_page')
  return skills


def get_certificates(request, profile):
  certificates = filter_category(request, profile.certificates.all(), 'certificate_category')
  certificates = search_certificate(request, certificates)
  certificates = pagination(request, certificates, 5, 'certificate_page')
  return certificates


def get_projects(request, profile):
  projects = search_project(request, profile.projects.all())
  projects = pagination(request, projects, 5, 'project_page')
  return projects


def get_experiences(request, profile):
  experiences = search_experience(request, profile.experiences.all())
  experiences = pagination(request, experiences, 5, 'experience_page')
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


def filter_category(request, objects, query):
  category = request.GET.get(query, '')
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


def pagination(request, object_list, amount, query):
  paginator = Paginator(object_list, amount)
  page = request.GET.get(query)
  try:
    objects = paginator.page(page)
  except PageNotAnInteger:
    objects = paginator.page(1)
  except EmptyPage:
    objects = paginator.page(paginator.num_pages)
  return objects
