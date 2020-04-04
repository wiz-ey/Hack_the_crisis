from django.urls import path
from . import views


urlpatterns = [


    path('update/<int:pk>/', UpdateLogs.as_view(), name='update_view'),
    path('risk/<int:pk>/', views.risk_marker, name='risk_view')




]
