from django.shortcuts import *
from rest_framework.decorators import api_view
# import .utils
# Create your views here.
from django.contrib.auth.decorators import login_required


# @api_view(['GET'])
def index(request):
	return HttpResponse("hello")

@api_view(['GET'])
def test(request):
	user = request.user
	return HttpResponse("hello world in test route " + str(user))
