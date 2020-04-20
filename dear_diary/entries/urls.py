
from django.urls import path
from . import views
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path( '', views.index,name='home'),
    path( 'add/',views.add, name='add'),
    path('delete/<int:entry_id>',views.delete_entry, name='delete')
]