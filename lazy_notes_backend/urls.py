from django.conf.urls import url, include

from rest_framework_jwt.views import obtain_jwt_token
# Serializers define the API representation.
from rest_framework import routers, viewsets
from api_auth.models import *
from rest_framework_mongoengine import serializers



class ToolSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Tool
        fields = '__all__'
# ViewSets define the view behavior.

from rest_framework_mongoengine import viewsets

class ToolViewSet(viewsets.ModelViewSet):
    '''
    Contains information about inputs/outputs of a single program
    that may be used in Universe workflows.
    '''
    lookup_field = 'id'
    serializer_class = ToolSerializer

    def get_queryset(self):
        return Tool.objects.all()

	

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'^tools', ToolViewSet, 'tools')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
	# url(r'^tets',views.test, namespace='test'),
    url(r'^', include(router.urls)),
     url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]