from django.contrib import admin
from .models import Profile, Skill

class ProfileAdmin(admin.ModelAdmin):
  model = Profile
  list_display = ['first_name', 'last_name', 'academic_formation', 'course']

class SkillAdmin(admin.ModelAdmin):
  list_display = ['title', 'priority', 'level', 'created_at']
  search_fields = ['title', 'description']
  list_filter = ['created_at']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Skill, SkillAdmin)
