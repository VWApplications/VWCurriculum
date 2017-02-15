from django.test import TestCase, Client, override_settings
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib import messages
from django.core import mail
from model_mommy import mommy
from vwcurriculum.core.models import Profile


@override_settings (
  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [],
          'APP_DIRS': True,
          'OPTIONS': {
              'context_processors': [
                  'django.template.context_processors.debug',
                  'django.template.context_processors.request',
                  'django.contrib.auth.context_processors.auth',
                  'django.contrib.messages.context_processors.messages',
              ],
          },
      },
  ]
)


class ContactTestCase(TestCase):

  def setUp(self):
    profile = mommy.make(Profile)
    self.client = Client()
    self.url = reverse('core:home')

  def test_form_errors(self):
    data = {'name': '', 'message': '', 'email': ''}
    response = self.client.post(self.url, data)
    self.assertFormError(response, 'form', 'name', 'Este campo é obrigatório.' )
    self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.' )
    self.assertFormError(response, 'form', 'message', 'Este campo é obrigatório.' )

  def test_form_correct(self):
    data = {'name': 'Pedro Calile', 'message': 'Mensagem de teste', 'email': 'pedro@gmail.com'}
    response = self.client.post(self.url, data)
    self.assertEquals(len(mail.outbox), 1)
    self.assertEquals(mail.outbox[0].subject, 'VWCurriculum: E-mail do [%s]' % data['name'])
    self.assertEquals(mail.outbox[0].to, [settings.CONTACT_EMAIL])
    self.assertEquals(mail.outbox[0].from_email, data['email'])
