from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('whatsAppMessage-list/', views.whatsAppMessageList, name='whatsAppMessage-list'),
    path('whatsAppMessage-view/<str:pk>/', views.whatsAppMessageView, name='whatsAppMessage-view'),
    path('whatsAppMessage-receive/', views.whatsAppMessageReceive, name='whatsAppMessage-receive'),

]