from django.urls import path
from .views import Login,Registration
urlpatterns = [
    path('signin/',Login.as_view(),name='signin'),
    path('signup/',Registration.as_view(),name='signup'),
]
