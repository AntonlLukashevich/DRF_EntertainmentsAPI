from django.urls import path
from . import views


urlpatterns = [
    path('entertainments/', views.EntertainmentsViewSet.as_view(), name='entertainments'),
]
