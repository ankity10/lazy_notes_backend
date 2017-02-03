from django.conf.urls import url, include
from rest_framework_jwt.views import *
from backend_app.views import * 
from django.contrib import admin
from realtime import views
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^$',  views.about, name='about'),
    url(r'^new/$', views.new_room, name='new_room'),
    url(r'^(?P<label>[\w-]{,50})/$', views.chat_room, name='chat_room'),

	url(r'^$', index, name='home-page'),
	url(r'^test$', test, name='test'),
	url(r'^api-token-refresh/', refresh_jwt_token),
	 url(r'^api-token-verify/', verify_jwt_token),
    url(r'^api-token-auth/', obtain_jwt_token, name='jwt-auth'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls)
]