from rest_framework.serializers import ModelSerializer
from .models import LernModulesModel


class LernModuleSerializer(ModelSerializer):
    class Meta:
        model = LernModulesModel
        fields = ['id', 'name', 'description', 'number']
