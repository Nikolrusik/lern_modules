from rest_framework.viewsets import ModelViewSet
from .models import LernModulesModel
from .serializers import LernModuleSerializer


class LernModuleViewSet(ModelViewSet):
    queryset = LernModulesModel.objects.all()
    serializer_class = LernModuleSerializer