import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator


class Profile(models.Model):
  first_name = models.CharField('Nome', max_length=100)
  last_name = models.CharField('Sobrenome', max_length=100)
  email = models.EmailField('Email')
  date_of_birth = models.DateField('Data de nascimento')
  about = models.TextField('Sobre mim', blank=True)
  current_work = models.CharField('Trabalho Atual', max_length=100, blank=True, default="Disponível")
  academic_formation = models.CharField('Formação Academica', max_length=100, blank=True)
  school_formation = models.CharField('Ensino Médio', max_length=100, blank=True)
  course = models.CharField('Curso', max_length=100, blank=True)
  languages = models.CharField('Idiomas', max_length=100, blank=True)
  address = models.CharField('Endereço', max_length=100, blank=True)
  phone = models.CharField('Telefone', max_length=100, blank=True)
  photo = models.ImageField(upload_to='imagens', verbose_name="Foto", blank=True, null=True)
  tags = models.CharField('Tags', max_length=100, blank=True)

  def get_age(self):
    today = datetime.date.today()
    birth = self.date_of_birth
    if today.month >= birth.month:
      if today.day >= birth.day:
        return today.year - birth.year
      else:
        return today.year - birth.year - 1
    else:
      return today.year - birth.year - 1

  def __str__(self):
    return self.first_name

  class Meta:
    verbose_name = 'Perfil'
    verbose_name_plural = 'Perfis'


class Skill(models.Model):
  title = models.CharField('Título', max_length=100)
  level = models.IntegerField('Nível', default=0, blank=True, null=True, validators=[MaxValueValidator(5), MinValueValidator(0)])
  description = models.TextField('Descrição', blank=True)
  priority = models.IntegerField('Prioridade', default=1, blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(10)])
  profile = models.ForeignKey(Profile, verbose_name='Perfil', related_name='skills')
  created_at = models.DateTimeField('Criado em', auto_now_add=True)
  updated_at = models.DateTimeField('Modificado em', auto_now=True)
  DEFAULT = 'Outras'
  CATEGORY = (
    ('Linguagens', 'Linguagens'),
    ('Framework', 'Framework'),
    ('Design', 'Design'),
    ('Devops', 'Devops'),
    ('Governança de TI', 'Governança de TI'),
    (DEFAULT, DEFAULT),
  )
  category = models.CharField('Categoria', max_length=100, choices=CATEGORY, default=DEFAULT)

  def __str__(self):
    return self.title

  class Meta:
    verbose_name = 'Habilidade'
    verbose_name_plural = 'Habilidades'
    ordering = ['priority', 'title', 'category', 'created_at']


class Certificate(models.Model):
  title = models.CharField('Título', max_length=100)
  issuing_institution = models.CharField('Orgão Emissor', max_length=100)
  url = models.URLField('URL do certificado', blank=True, null=True, help_text='URL official do certificado')
  document = models.URLField('URL do certificado', max_length=1000, help_text='URL do google driver do certificado,na imagem clique com o botão direito, depois clique em share e coloque o link no navegador, após isso clique com o botão direito na imagem e copy image address e cole aqui')
  profile = models.ForeignKey(Profile, verbose_name='Perfil', related_name='certificates')
  created_at = models.DateTimeField('Criado em', auto_now_add=True)
  updated_at = models.DateTimeField('Modificado em', auto_now=True)
  DEFAULT = _('Others')
  CATEGORY = (
    (_('Languages'), _('Languages')),
    (_('Framework'), _('Framework')),
    (_('Design'), _('Design')),
    (_('Devops'), _('Devops')),
    (_('Management'), _('Management and Business')),
    (DEFAULT, DEFAULT),
  )
  category = models.CharField('Categoria', max_length=100, choices=CATEGORY, default=DEFAULT)

  def __str__(self):
    return self.title

  class Meta:
    verbose_name = 'Certificado'
    verbose_name_plural = 'Certificados'
    ordering = ['title', 'issuing_institution', 'category', 'created_at']


class Project(models.Model):
  title = models.CharField('Título', max_length=100)
  position = models.CharField('Cargo', max_length=100, help_text='Cargo ocupado no projeto')
  institution = models.CharField('Instituição', max_length=100, help_text='Instituição que realizou ou contratou o projeto')
  start_date = models.DateField('Data de inicio')
  end_date = models.DateField('Data de termino', blank=True, null=True)
  url = models.URLField('Link', help_text='URL do projeto', blank=True, null=True)
  description = models.TextField('Descrição')
  is_voluntary = models.BooleanField('É voluntario?', default=False)
  profile = models.ForeignKey(Profile, verbose_name='Perfil', related_name='projects')
  created_at = models.DateTimeField('Criado em', auto_now_add=True)
  updated_at = models.DateTimeField('Modificado em', auto_now=True)
  DEFAULT_STATUS = _('In progress')
  STATUS = (
    (_('Completed'), _('Completed')),
    (DEFAULT_STATUS, DEFAULT_STATUS),
    (_('Stopped'), _('Stopped')),
    (_('Canceled'), _('Canceled')),
  )
  situation = models.CharField('Situação', max_length=100, choices=STATUS, default=DEFAULT_STATUS, help_text='Situação do projeto')

  def __str__(self):
    return self.title

  class Meta:
    verbose_name = 'Projeto'
    verbose_name_plural = 'Projetos'
    ordering = ['start_date', 'title']


class Experience(models.Model):
  title = models.CharField('Título', max_length=100)
  short_title = models.CharField('Abreveatura', max_length=100, help_text='Abreveatura do título')
  location = models.CharField('Local', max_length=100, help_text='Local que foi adquirido a experiencia ou trabalho')
  start_date = models.DateField('Data de Início')
  end_date = models.DateField('Data de Termino', blank=True, null=True)
  description = models.TextField('Descrição', blank=True)
  is_current_job = models.BooleanField('É o trabalho atual?', default=False)
  event_url = models.URLField('URL do evento', blank=True, null=True, help_text='URL do certificado do evento ou do evento em si')
  profile = models.ForeignKey(Profile, verbose_name='Perfil', related_name='experiences')
  created_at = models.DateTimeField('Criado em', auto_now_add=True)
  updated_at = models.DateTimeField('Modificado em', auto_now=True)

  def __str__(self):
    return self.short_title

  class Meta:
    verbose_name = 'Experiência'
    verbose_name_plural = 'Experiências'
    ordering = ['start_date', 'title']


class File(models.Model):
  title = models.CharField('Título', max_length=100, help_text='Título do projeto')
  document = models.FileField(upload_to='documentos', verbose_name='Documentos', blank=True, null=True)
  project = models.ForeignKey(Project, verbose_name='Projeto', related_name='files', null=True)
  experience = models.ForeignKey(Experience, verbose_name='Experiência', related_name='files', null=True)

  def __str__(self):
    return self.title

  class Meta:
    verbose_name = "Arquivo"
    verbose_name_plural = "Arquivos"
    ordering = ['title']


class Interest(models.Model):
  title = models.CharField('Área de Interesse', max_length=100)
  description = models.TextField('Descrição')
  profile = models.ForeignKey(Profile, verbose_name='Perfil', related_name='interests')
  fa_icon = models.CharField('Icone Font Awesome', max_length=100, blank=True, help_text='Inserir os icones do font awesome em http://fontawesome.io/ ou http://www.w3schools.com/icons/fontawesome_icons_intro.asp')
  created_at = models.DateTimeField('Criado em', auto_now_add=True)
  updated_at = models.DateTimeField('Modificado em', auto_now=True)

  def __str__(self):
    return self.title

  class Meta:
    verbose_name = 'Área de Interesse'
    verbose_name_plural = 'Áreas de interesse'
    ordering = ['title']


class Link(models.Model):
  title = models.CharField('Título', max_length=100)
  link = models.URLField('Link')
  fa_icon = models.CharField('Icone Font Awesome', max_length=100, blank=True, help_text='Inserir os icones do font awesome em http://fontawesome.io/ ou http://www.w3schools.com/icons/fontawesome_icons_intro.asp')
  profile = models.ForeignKey(Profile, verbose_name='Perfil', related_name='links')

  def __str__(self):
    return self.link

  class Meta:
    verbose_name = 'Link'
    verbose_name_plural = 'Links'
    ordering = ['title']
