import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from mixer.backend.django import mixer
from django.forms.models import model_to_dict
from lern_module.views import LernModuleViewSet
from lern_module.models import LernModulesModel
from lern_module.serializers import LernModuleSerializer


class TestLernModuleViewSet(APITestCase):
    '''
    Tests CRUD for views
    '''

    def setUp(self):
        self.obj = mixer.blend(LernModulesModel)
        self.obj_url = f'/api/lern_module/{self.obj.id}/'
        self.url = '/api/lern_module/'

    def test_get_data(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_data(self):
        new_data = model_to_dict(mixer.blend(LernModulesModel))
        new_data['description'] = 'descr'
        response = self.client.put(self.obj_url, data=new_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_data(self):
        new_data = model_to_dict(mixer.blend(LernModulesModel))
        new_data['description'] = 'descr'
        response = self.client.post(self.url, data=new_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_data(self):
        response = self.client.delete(self.obj_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TestLernModuleModel(TestCase):
    '''
    Tests for model
    '''

    def setUp(self):
        self.obj1 = mixer.blend(LernModulesModel)
        self.obj2 = mixer.blend(LernModulesModel)

    def test_objects_count(self):
        self.assertEqual(LernModulesModel.objects.count(), 2)

    def test_object_creation(self):
        obj = mixer.blend(LernModulesModel)
        self.assertTrue(obj.id is not None)

    def test_object_retrieval(self):
        obj = LernModulesModel.objects.get(id=self.obj1.id)
        self.assertEqual(obj.description, None)

    def test_object_update(self):
        self.obj1.name = "New name"
        self.assertTrue(self.obj1.name == 'New name')


class TestSerializer(TestCase):
    '''
    Tests for serializer
    '''

    def setUp(self):
        self.instance = LernModulesModel.objects.create(
            name="Name", description="Descr", number="A101")
        self.serializer = LernModuleSerializer(instance=self.instance)

    def test_serializer_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(
            ['id', 'name', 'description', 'number']))
        self.assertEqual(data['id'], self.instance.id)
        self.assertEqual(data['name'], self.instance.name)

    def test_deserialization(self):
        new_data = {'name': 'name', 'description': 'descr', 'number': 'number'}
        serializer = LernModuleSerializer(data=new_data)
        self.assertTrue(serializer.is_valid())
        obj = serializer.save()
        self.assertEqual(obj.name, 'name')
