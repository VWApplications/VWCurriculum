from django.contrib import admin
from .models import Profile, Link, File, Skill, Certificate, Project, Experience, Interest


class LinkInlineAdmin(admin.StackedInline):
  model = Link


class FileInlineAdmin(admin.StackedInline):
  model = File
  fields = ['title', 'document']


class ProfileAdmin(admin.ModelAdmin):
  list_display = ['first_name', 'last_name', 'academic_formation', 'course']
  inlines = [LinkInlineAdmin]


class SkillAdmin(admin.ModelAdmin):
  list_display = ['title', 'priority', 'level', 'category', 'created_at']
  search_fields = ['title', 'description']
  list_filter = ['created_at', 'category']


class CertificateAdmin(admin.ModelAdmin):
  list_display = ['title', 'issuing_institution', 'category', 'created_at']
  search_fields = ['title', 'issuing_institution']
  list_filter = ['created_at', 'category']


class ProjectAdmin(admin.ModelAdmin):
  list_display = ['title', 'position', 'institution', 'start_date', 'is_voluntary', 'situation']
  search_fields = ['title', 'institution', 'description']
  list_filter = ['start_date', 'is_voluntary', 'situation']
  inlines = [FileInlineAdmin]


class ExperienceAdmin(admin.ModelAdmin):
  list_display = ['short_title', 'location', 'start_date', 'is_current_job']
  search_fields = ['short_title', 'title', 'description']
  list_filter = ['start_date']
  inlines = [FileInlineAdmin]


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Interest)
