from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Profile(models.Model):
  first_name = models.CharField('Nome', max_length=100)
  last_name = models.CharField('Sobrenome', max_length=100)
  age = models.IntegerField('Idade', blank=True)
  about = models.TextField('Sobre mim', blank=True)
  current_work = models.CharField('Trabalho Atual', max_length=100, blank=True, default="Disponível")
  academic_formation = models.CharField('Formação Academica', max_length=100, blank=True)
  course = models.CharField('Curso', max_length=100, blank=True)
  languages = models.CharField('Idiomas', max_length=100, blank=True)
  photo = models.ImageField(upload_to='images', verbose_name="Foto", blank=True, null=True)

  def __str__(self):
    return self.first_name

  class Meta:
    verbose_name = 'Perfil'
    verbose_name_plural = 'Perfis'


class Skill(models.Model):
  title = models.CharField('Título', max_length=100)
  level = models.IntegerField('Nível', default=0, blank=True, null=True, validators=[MaxValueValidator(5), MinValueValidator(0)])
  description = models.TextField('Descrição', blank=True)
  priority = models.IntegerField('Prioridade', default=1, blank=True, null=True, validators=[MinValueValidator(1)])
  created_at = models.DateTimeField('Criado em', auto_now_add=True)
  updated_at = models.DateTimeField('Modificado em', auto_now=True)

  def __str__(self):
    return self.title

  class Meta:
    verbose_name = 'Habilidade'
    verbose_name_plural = 'Habilidades'
    ordering = ['priority', 'title', 'created_at']
