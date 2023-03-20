from rest_framework.serializers import ModelSerializer
from .models import Position, Skill, Application, PositionSkill, ApplicationSkill, ApplicationPosition

class SkillSerializer(ModelSerializer):
    class Meta:
        model = Skill
        fields = [
            'id', 
            'name'
            ]

class PositionSkillSerializer(ModelSerializer):
    class Meta:
        model = PositionSkill
        fields = [
            'position', 
            'skill'
        ]

class PositionSerializer(ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)
    class Meta:
        model = Position
        fields = [
            'id',
            'name',
            'skills'
        ]

class ApplicationSkillSerializer(ModelSerializer):
    class Meta:
        model = ApplicationSkill
        fields = '__all__'

class ApplicationPositionSerializer(ModelSerializer):
    class Meta:
        model = ApplicationPosition
        fields = '__all__'

class ApplicationSerializer(ModelSerializer):
    # populates the specified fields
    # many=True when retrieving a list
    skills = SkillSerializer(many=True, read_only=True)
    positions = PositionSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Application
        fields = ['user', 
            'bio', 
            'skills', 
            'education', 
            'experience', 
            'positions', 
            'status']
        # is_highlighted and status is changed by admin

    def create(self, validated_data):
        skills_context = self.context.get('request').data.get('skills')
        positions_context = self.context.get('request').data.get('positions')

        new_application = Application.objects.create(**validated_data)

        if skills_context:
            skills = Skill.objects.filter(id__in=skills_context)
            new_application.skills.set(skills)
            new_application.save()
        
        if positions_context:
            positions = Position.objects.filter(id__in=positions_context)
            new_application.positions.set(positions)
            new_application.save()

        return new_application

class ApplicationStatusUpdateGenericSerializer(ModelSerializer):
    class Meta:
        model = Application
        fields = ['status']

class ApplicationStatusUnreadUpdateSerializer(ApplicationStatusUpdateGenericSerializer):
    def update(self, instance, validated_data, *args, **kwargs):
        instance.set_unread_status()
        return super().update(instance, validated_data, *args, **kwargs)

class ApplicationStatusReadUpdateSerializer(ApplicationStatusUpdateGenericSerializer):
    def update(self, instance, validated_data, *args, **kwargs):
        instance.set_read_status()
        return super().update(instance, validated_data, *args, **kwargs)
    
class ApplicationStatusInterview1UpdateSerializer(ApplicationStatusUpdateGenericSerializer):
    def update(self, instance, validated_data, *args, **kwargs):
        instance.set_interview_1_status()
        return super().update(instance, validated_data, *args, **kwargs)

class ApplicationStatusInterview2UpdateSerializer(ApplicationStatusUpdateGenericSerializer):
    def update(self, instance, validated_data, *args, **kwargs):
        instance.set_interview_2_status()
        return super().update(instance, validated_data, *args, **kwargs)

class ApplicationStatusInterview3UpdateSerializer(ApplicationStatusUpdateGenericSerializer):
    def update(self, instance, validated_data, *args, **kwargs):
        instance.set_interview_3_status()
        return super().update(instance, validated_data, *args, **kwargs)

class ApplicationStatusAcceptedUpdateSerializer(ApplicationStatusUpdateGenericSerializer):
    def update(self, instance, validate_data, *args, **kwargs):
        instance.set_accepted_status()
        return super().update(instance, validate_data, *args, **kwargs)

class ApplicationStatusRejectedUpdateSerializer(ApplicationStatusUpdateGenericSerializer):
    def update(self, instance, validate_data, *args, **kwargs):
        instance.set_rejected_status()
        return super().update(instance, validate_data, *args, **kwargs)

class ApplicationStatusArchivedUpdateSerializer(ApplicationStatusUpdateGenericSerializer):
    def update(self, instance, validate_data, *args, **kwargs):
        instance.set_archived_status()
        return super().update(instance, validate_data, *args, **kwargs)