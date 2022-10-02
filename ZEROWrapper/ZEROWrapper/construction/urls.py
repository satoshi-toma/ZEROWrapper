from django.urls import path
from .views import ConstructionListView


app_name = 'construction'
urlpatterns = [
    path('construction_list/', ConstructionListView.as_view(), name='construction_list'),
]