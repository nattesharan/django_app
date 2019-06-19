from django.shortcuts import redirect, reverse
from django.http import JsonResponse
from google.cloud import pubsub_v1
from google.oauth2 import service_account
from django.conf import settings
from rest_framework.decorators import api_view
import json
from rest_framework.parsers import JSONParser

def main(request):
    return redirect(reverse('accounts:login'))

def publisher(request):
    # we can set the credentials in two ways either with envirornment variable or creating with google.oauth2
    # import os
    # os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/path/to/file.json"
    credentials = service_account.Credentials.from_service_account_file(settings.GOOGLE_APPLICATION_CREDENTIALS)
    publisher = pubsub_v1.PublisherClient(credentials=credentials)
    topic = 'projects/{project}/topics/{topic}'.format(project=settings.PROJECT, topic=settings.TOPIC)
    message = bytes(json.dumps({'name': 'test pubsub', 'status': True}), encoding='utf8')
    # response = publisher.publish(topic, data=message)
    # to publish attributes
    response = publisher.publish(topic, data=message, name="Hey", id=str(32), age=str(23))
    print(response.result())
    return JsonResponse({'status': True, 'message': 'It works'}, status=201)

@api_view(['POST'])
def pub_sub_callback(request):
    data = request.data
    print(data)
    return JsonResponse({'status': True})