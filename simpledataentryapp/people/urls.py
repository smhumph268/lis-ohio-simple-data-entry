from django.urls import path
from . import views

app_name = 'people'

urlpatterns = [
    path('new', views.new_user, name='new'),
    path('confirmation/<int:person_id>', views.confirmation, name='confirmation')
]
