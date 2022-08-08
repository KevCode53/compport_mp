from django.urls import path
from .views import MaintenancePDFView

urlpatterns = [
    path('report/', MaintenancePDFView, name='maintenance_pdf'),
]
