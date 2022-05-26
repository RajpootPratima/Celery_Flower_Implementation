from django.shortcuts import render
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
from .tasks import *

class CeleryCheck(APIView):
    def post(self,request,format=None):
        try:
            message = {"num":request.data['num']}
            result = process_request.apply_async(queue='celery',args=(message,))
            return Response({
                'status':200,
                'message':"REQUEST SUBMITTED",
                'task_id': result.task_id})
        except Exception as e:
            return Response({
                'code':500,
                'status':"Exception Occured",
                'message':str(e)},
                status= status.HTTP_500_INTERNAL_SERVER_ERROR)

