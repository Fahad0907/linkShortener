from django.urls import path
from .views import LinkList
urlpatterns = [
    
    path('', LinkList.as_view(),name='linklist'),
]
