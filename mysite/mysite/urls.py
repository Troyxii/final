from django.contrib import admin
from django.urls import path
from polls.views import home, events, admins, updateeve, deleteve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name=''),
    path('events/', events, name='events'),
    path('deleteve/<int:id>/', deleteve, name='deleteve'),
    path('updateeve/<int:id>/', updateeve, name='updateeve'),
    path('admins/', admins, name='admins')
]


