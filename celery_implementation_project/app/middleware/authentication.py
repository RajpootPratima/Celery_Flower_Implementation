from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse
from django.conf import settings
from django.urls import resolve

class HeaderAuthMW(MiddlewareMixin):
    jwToken = ''

    def validate_token(self, auth_token):
        if auth_token == settings.AUTH_TOKEN:
            return ""

    def process_request(self,request):
        token = request.headers.get('Authorization',None)
        if token:
            self.validate_token(token)
            return self.validate_token(token)
        else:
            return HttpResponse("Authorization missing in header",status=401)

    def process_response(self,request,response):
        current_url = resolve(request.path_info).url_name
        if hasattr(response,'data'):
            self.log('response',str(response.data),1,response.status_code,None,None,str(""))
        else:
            self.log('response', None, 0, response.status_code, None, None, str(""))
        return response

