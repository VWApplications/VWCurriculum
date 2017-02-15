import datetime
from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from vwcurriculum.core.models import Profile, Skill, Certificate, Project, Experience
from model_mommy import mommy


class ModelsTestCase(TestCase):

  def setUp(self):
    self.profile = mommy.make(Profile, date_of_birth=datetime.date(1993, 8, 21))
    self.skills = mommy.make(Skill, profile=self.profile, _quantity=15)
    self.certificates = mommy.make(Certificate, profile=self.profile, _quantity=9)
    self.projects = mommy.make(Project, profile=self.profile, _quantity=12)
    self.experiences = mommy.make(Experience, profile=self.profile, _quantity=3)

  def tearDown(self):
    Profile.objects.all().delete()
    Skill.objects.all().delete()
    Certificate.objects.all().delete()
    Project.objects.all().delete()
    Experience.objects.all().delete()

  def test_create_models(self):
    self.assertEquals(len(self.skills), 15)
    self.assertEquals(len(self.certificates), 9)
    self.assertEquals(len(self.projects), 12)
    self.assertEquals(len(self.experiences), 3)

  def test_profile_get_age(self):
    self.assertEquals(self.profile.get_age(), 23)
