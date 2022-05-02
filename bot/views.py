from email import message
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import WhatsAppMessageSerializer

from twilio.rest import Client
from django.views.decorators.csrf import csrf_exempt

from rest_framework_simplejwt.tokens import RefreshToken

from .models import WhatsAppMessage

import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.


account_sid = os.environ.get('ACCOUNT_SID')
auth_token = os.environ.get('AUTH_TOKEN')
auth_token = '948e681805723cffd5ddbca379a424dc'
client = Client(account_sid, auth_token)

# Create your views here.


@api_view(['GET', 'POST'])
def apiOverview(request):
    api_urls = {
        'List': '/whatsAppMessage-list/',
        'Create': '/whatsAppMessage-create',
        'View': '/whatsAppMessage-view/<str:pk>/',
        'Receive': '/whatsAppMessage-receive/'
    }
    return Response(api_urls)

@api_view(['GET', 'POST'])
def whatsAppMessageList(request):
    whatsAppMessages = WhatsAppMessage.objects.all()
    serializer = WhatsAppMessageSerializer(whatsAppMessages, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def whatsAppMessageView(request, pk):
    whatsAppMessages = WhatsAppMessage.objects.get(id=pk)
    serializer = WhatsAppMessageSerializer(whatsAppMessages, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def whatsAppMessageCreate(request):
    msg = WhatsAppMessage(messageSender="1023456789", messageBody='hELO')
    msg.save()
    print(msg)
    print(request.data)
    serializer = WhatsAppMessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
@csrf_exempt
def whatsAppMessageReceive(request):
    messageSender = request.data['From']
    messageBody = request.data['Body']
    newWhatsAppMessage = WhatsAppMessage(messageSender=messageSender, messageBody=messageBody)
    newWhatsAppMessage.save()

    if request.data:
        client.messages.create(
            from_='whatsapp:+14155238886',
            body='Hey There {}! Welcome to my WhatsApp bot'.format(messageSender),
            to=messageSender,
        )


    return HttpResponse('hello')

@api_view(['POST'])
def whatsAppMessageAccessToken(user):
    refresh = RefreshToken.for_user(user)

    return {
        'access': str(refresh.access_token),
    }

