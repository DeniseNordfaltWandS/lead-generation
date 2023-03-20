from rest_framework.serializers import ModelSerializer
from .models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name', 
            'last_name',
            'email', 
            'phone_number', 
            'born_at', 
            'address', 
            'languages', 
            'linkedin_url', 
            'github_url', 
            'portfolio_url'
            ]