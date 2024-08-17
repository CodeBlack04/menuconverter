from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework.views import APIView

# Create your views here.
class ProcessImage(APIView):
    def get(request):
        result = {
            'data': [],
            'message': 'Success',
            'status': HTTP_200_OK
        }


        return Response(result, status=HTTP_200_OK)