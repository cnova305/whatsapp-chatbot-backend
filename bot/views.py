from email import message
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import WhatsAppMessageSerializer

from twilio.rest import Client
from django.views.decorators.csrf import csrf_exempt

from .models import WhatsAppMessage

account_sid = 'ACfed9835a3dfdd5eb7c7e29ce1da3980e'
auth_token = '96cb14f4af6dc9197a719f88a9a20d87'
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


    return HttpResponse('hello')