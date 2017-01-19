from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token
from backend_app.views import * 

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
	url(r'^$', index, namespace='home-page'),
    url(r'^api-token-auth/', obtain_jwt_token, namespace='jwt-auth'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]