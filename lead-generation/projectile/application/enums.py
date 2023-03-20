from django.db import models
from django.utils.translation import gettext_lazy as _

class SeniorityEnum(models.TextChoices):
    NOOB = '0-1',_('Noob')
    JUNIOR = '1-3',_('Junior')
    SENIOR = '3+',_('Senior')

class StatusEnum(models.TextChoices):
    UNREAD = _('Unread')
    READ = _('Read')
    INTERVIEW_1 = _('Interview 1')
    INTERVIEW_2 = _('Interview 2')
    INTERVIEW_3 = _('Interview 3')
    ACCEPTED = _('Accepted')
    REJECTED = _('Rejected')
    ARCHIVED = _('Archived')

