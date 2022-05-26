from celery_implementation_project import celery_app
import traceback , math
@celery_app.task(serializer='json')
def process_request(request,*args,**kwargs):
    try:
        num = request.get('num')
        res = find_factorial(num)
    except Exception as e:
        print(traceback.format_exc())

def find_factorial(num):
    return math.factorial(num)


