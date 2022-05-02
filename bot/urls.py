from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('whatsAppMessage-list/', views.whatsAppMessageList, name='whatsAppMessage-list'),
    path('whatsAppMessage-view/<str:pk>/', views.whatsAppMessageView, name='whatsAppMessage-view'),
    path('whatsAppMessage-receive/', views.whatsAppMessageReceive, name='whatsAppMessage-receive'),
    path('whatsAppMessage-token/', views.whatsAppMessageAccessToken, name='whatsAppMessage-token'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]