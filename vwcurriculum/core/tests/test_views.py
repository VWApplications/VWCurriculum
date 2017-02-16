import datetime
from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from vwcurriculum.core.models import Profile, Skill, Certificate, Project, Experience
from django.core.paginator import Paginator
from model_mommy import mommy


class HomeViewTestCase(TestCase):

  def setUp(self):
    profile = mommy.make(Profile)
    self.skills = mommy.make(Skill, profile=profile, _quantity=15)
    self.certificates = mommy.make(Certificate, profile=profile, _quantity=9)
    self.projects = mommy.make(Project, profile=profile, _quantity=12)
    self.experiences = mommy.make(Experience, profile=profile, _quantity=3)
    self.client = Client()
    self.url = reverse('core:home')

  def tearDown(self):
    Profile.objects.all().delete()
    Skill.objects.all().delete()
    Certificate.objects.all().delete()
    Project.objects.all().delete()
    Experience.objects.all().delete()

  def test_status_code_200(self):
    response = self.client.get(self.url)
    self.assertEquals(response.status_code, 200)

  def test_template_used(self):
    response = self.client.get(reverse('core:home'))
    self.assertTemplateUsed(response, 'core/base.html')
    self.assertTemplateUsed(response, 'core/footer.html')
    self.assertTemplateUsed(response, 'core/home.html')
    self.assertTemplateUsed(response, 'core/certificates.html')
    self.assertTemplateUsed(response, 'core/experiences.html')
    self.assertTemplateUsed(response, 'core/navbar.html')
    self.assertTemplateUsed(response, 'core/pagination.html')
    self.assertTemplateUsed(response, 'core/profile.html')
    self.assertTemplateUsed(response, 'core/projects.html')
    self.assertTemplateUsed(response, 'core/skills.html')

  def test_context(self):
    response = self.client.get(self.url)
    self.assertTrue('skills' in response.context)
    self.assertTrue('certificates' in response.context)
    self.assertTrue('projects' in response.context)
    self.assertTrue('experiences' in response.context)
    self.assertTrue('form' in response.context)
    self.assertTrue('request' in response.context)
    self.assertTrue('paginator' in response.context)
    self.assertTrue('user' in response.context)


class SkillTestCase(TestCase):

  def setUp(self):
    profile = mommy.make(Profile)
    mommy.make(Skill, profile=profile, _quantity=7, category="Framework")
    mommy.make(Skill, profile=profile, _quantity=8, category="Design")
    mommy.make(Skill, profile=profile, _quantity=2, category="Linguagens")
    mommy.make(Skill, profile=profile, _quantity=8, category="Governança de TI")
    mommy.make(Skill, profile=profile, _quantity=6, category="Outras")
    self.client = Client()
    self.url = reverse('core:home')

  def tearDown(self):
    Profile.objects.all().delete()
    Skill.objects.all().delete()

  def test_skills_pagination(self):
    response = self.client.get(self.url)
    paginator = response.context['paginator']
    skills = response.context['skills']
    self.assertEquals(paginator.count, 31)
    self.assertEquals(paginator.per_page, 20)
    self.assertEquals(paginator.num_pages, 2)
    self.assertEquals(len(skills), 20)

  def test_skills_filter(self):
    response = self.client.get('{0}?skill_category=Framework'.format(self.url))
    skills = response.context['skills']
    self.assertEquals(len(skills), 7)
    response = self.client.get('{0}?skill_category=Design'.format(self.url))
    skills = response.context['skills']
    self.assertEquals(len(skills), 8)
    response = self.client.get('{0}?skill_category=Devops'.format(self.url))
    skills = response.context['skills']
    self.assertEquals(len(skills), 0)
    response = self.client.get('{0}?skill_category=Linguagens'.format(self.url))
    skills = response.context['skills']
    self.assertEquals(len(skills), 2)
    response = self.client.get('{0}?skill_category=Governanca'.format(self.url))
    skills = response.context['skills']
    self.assertEquals(len(skills), 8)
    response = self.client.get('{0}?skill_category=Outras'.format(self.url))
    skills = response.context['skills']
    self.assertEquals(len(skills), 6)


class CertificateTestCase(TestCase):

  def setUp(self):
    profile = mommy.make(Profile)
    mommy.make(Certificate, profile=profile, _quantity=2, category="Framework", title="Linguagem C")
    mommy.make(Certificate, profile=profile, _quantity=4, category="Design")
    mommy.make(Certificate, profile=profile, _quantity=2, category="Linguagens")
    mommy.make(Certificate, profile=profile, _quantity=8, category="Governança de TI")
    mommy.make(Certificate, profile=profile, _quantity=3, category="Outras")
    self.client = Client()
    self.url = reverse('core:home')

  def tearDown(self):
    Profile.objects.all().delete()
    Certificate.objects.all().delete()

  def test_certificate_pagination(self):
    response = self.client.get(self.url)
    paginator = response.context['paginator']
    certificates = response.context['certificates']
    self.assertEquals(len(certificates), 5)
    # self.assertEquals(paginator.num_pages, 4)
    # self.assertEquals(paginator.per_page, 5)
    # self.assertEquals(paginator.count, 19)

  def test_certificates_filter(self):
    response = self.client.get('{0}?certificate_category=Framework'.format(self.url))
    certificates = response.context['certificates']
    self.assertEquals(len(certificates), 2)
    response = self.client.get('{0}?certificate_category=Design'.format(self.url))
    certificates = response.context['certificates']
    self.assertEquals(len(certificates), 4)
    response = self.client.get('{0}?certificate_category=Devops'.format(self.url))
    certificates = response.context['certificates']
    self.assertEquals(len(certificates), 0)
    response = self.client.get('{0}?certificate_category=Linguagens'.format(self.url))
    certificates = response.context['certificates']
    self.assertEquals(len(certificates), 2)
    response = self.client.get('{0}?certificate_category=Governanca'.format(self.url))
    certificates = response.context['certificates']
    self.assertEquals(len(certificates), 5)
    response = self.client.get('{0}?certificate_category=Outras'.format(self.url))
    certificates = response.context['certificates']
    self.assertEquals(len(certificates), 3)

  def test_certificate_search(self):
    response = self.client.get('{0}?q_certificate=Linguagem+C'.format(self.url))
    certificates = response.context['certificates']
    self.assertEquals(len(certificates), 2)


class ProjectTestCase(TestCase):

  def setUp(self):
    profile = mommy.make(Profile)
    mommy.make(Project, profile=profile, _quantity=3, title="Projeto de cultura e lazer")
    mommy.make(Project, profile=profile, _quantity=9, title="Projeto PIBIC")
    self.client = Client()
    self.url = reverse('core:home')

  def tearDown(self):
    Profile.objects.all().delete()
    Project.objects.all().delete()

  def test_project_pagination(self):
    response = self.client.get(self.url)
    paginator = response.context['paginator']
    projects = response.context['projects']
    self.assertEquals(len(projects), 5)
    # self.assertEquals(paginator.count, 12)
    # self.assertEquals(paginator.per_page, 5)
    # self.assertEquals(paginator.num_pages, 3)

  def test_project_search(self):
    response = self.client.get('{0}?q_project=Projeto+de+cultura+e+lazer'.format(self.url))
    projects = response.context['projects']
    self.assertEquals(len(projects), 3)


class ExperienceTestCase(TestCase):

  def setUp(self):
    profile = mommy.make(Profile)
    mommy.make(Experience, profile=profile, _quantity=3, title="Hackthon")
    mommy.make(Experience, profile=profile, _quantity=9, title="PIBIC")
    self.client = Client()
    self.url = reverse('core:home')

  def tearDown(self):
    Profile.objects.all().delete()
    Experience.objects.all().delete()

  def test_experience_pagination(self):
    response = self.client.get(self.url)
    paginator = response.context['paginator']
    experiences = response.context['experiences']
    self.assertEquals(len(experiences), 5)
    # self.assertEquals(paginator.count, 12)
    # self.assertEquals(paginator.per_page, 5)
    # self.assertEquals(paginator.num_pages, 3)

  def test_project_search(self):
    response = self.client.get('{0}?q_experience=Hackthon'.format(self.url))
    experiences = response.context['experiences']
    self.assertEquals(len(experiences), 3)
