from django.db import models
from .enums import SeniorityEnum, StatusEnum
from common.abstracts import TimestampModel

class Skill(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'

class Position(models.Model):
    name = models.CharField(max_length=200)
    skills = models.ManyToManyField('Skill', through='PositionSkill')

    def __str__(self):
        return f'{self.name}'

class PositionSkill(models.Model):
    position = models.ForeignKey('Position', on_delete=models.CASCADE)
    skill = models.ForeignKey('Skill', on_delete=models.CASCADE)

class ApplicationPosition(models.Model):
    application = models.ForeignKey('Application', on_delete=models.CASCADE)
    position = models.ForeignKey('Position', on_delete=models.CASCADE)

# ärv created_at (TimeStampModel)
class Application(TimestampModel):
    user = models.ForeignKey('core.User', on_delete=models.CASCADE)
    bio = models.TextField(null=True,blank=True)
    skills = models.ManyToManyField('Skill', through='ApplicationSkill')
    education = models.TextField(null=True,blank=True)
    experience = models.TextField(null=True,blank=True)
    positions = models.ManyToManyField('Position', through='ApplicationPosition')
    status = models.CharField(max_length=50, choices=StatusEnum.choices, default=StatusEnum.UNREAD)
    is_highlighted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def set_unread_status(self):
        self.status = StatusEnum.UNREAD.value
    
    def set_read_status(self):
        self.status = StatusEnum.READ.value
    
    def set_interview_1_status(self):
        self.status = StatusEnum.INTERVIEW_1.value

    def set_interview_2_status(self):
        self.status = StatusEnum.INTERVIEW_2.value

    def set_interview_3_status(self):
        self.status = StatusEnum.INTERVIEW_3.value
    
    def set_accepted_status(self):
        self.status = StatusEnum.ACCEPTED.value
    
    def set_rejected_status(self):
        self.status = StatusEnum.REJECTED.value
    
    def set_archived_status(self):
        self.status = StatusEnum.ARCHIVED.value
    
    def __str__(self):
        return f'Application: {self.id} - {self.user}'

class ApplicationSkill(models.Model):
    skill = models.ForeignKey('Skill', on_delete=models.CASCADE)
    application = models.ForeignKey('Application', on_delete=models.CASCADE)
    seniority = models.CharField(max_length=200, choices=SeniorityEnum.choices, default=SeniorityEnum.NOOB)
