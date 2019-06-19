from django.conf import settings
from google.cloud import pubsub_v1
from google.oauth2 import service_account
import time
import json
import os
import requests

def show_message(message):
    address = 'http://localhost:8000/pubsub/callback/'
    message.ack()
    data = json.loads(message.data)
    attrs = message.attributes
    payload = {
        'data': data,
        'name': attrs['name'],
        'age': attrs['age'],
        'id': attrs['id']
    }
    reponse = requests.post(address, json=payload)

if __name__=='__main__':
    file = os.path.join(os.path.dirname(os.path.abspath(__file__)),'key.json')
    credentials = service_account.Credentials.from_service_account_file(file)
    subscriber1 = pubsub_v1.SubscriberClient(credentials=credentials)
    subscriber2 = pubsub_v1.SubscriberClient(credentials=credentials)
    subscription_1 = 'projects/{project}/subscriptions/{subscription}'.format(project='personal-243717', subscription='subscription1')
    subscription_2 = 'projects/{project}/subscriptions/{subscription}'.format(project='personal-243717', subscription='subscription2')
    subscriber1.subscribe(subscription_1, show_message)
    subscriber2.subscribe(subscription_2, show_message)
    while True:
        time.sleep(10)
        print("listening")
