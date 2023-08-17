from django.contrib import admin
from django.urls import path, include

from people import views as people_views

urlpatterns = [
    path('', people_views.new_user, name='index'),
    path('admin/', admin.site.urls),
    path('people/', include('people.urls'))
]
