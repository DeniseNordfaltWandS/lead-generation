from django.contrib import admin
from .models import Application, Skill, Position, PositionSkill, ApplicationPosition, ApplicationSkill

class PositionSkillInline(admin.TabularInline):
    model = PositionSkill
    extra = 1
    raw_id_fields = ('skill',)

class ApplicationPositionInline(admin.TabularInline):
    model = ApplicationPosition
    extra = 0
    raw_id_fields = ('position',)

class ApplicationSkillInline(admin.TabularInline):
    model = ApplicationSkill
    extra = 0
    raw_id_fields = ('skill',)

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)
    list_display = ('id', 'user', 'status',)
    inlines = [ApplicationPositionInline, ApplicationSkillInline]

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name',)
    inlines = [PositionSkillInline]
