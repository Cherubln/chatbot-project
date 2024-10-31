from django.urls import path
from .views import import_data_from_sheet

urlpatterns = [
    path('import_data_from_sheet/', import_data_from_sheet,
         name='import_data_from_sheet'),
]
