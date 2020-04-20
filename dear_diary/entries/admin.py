from django.contrib import admin
from .models import Entry

# allows me to see the model on the admin dash board
admin.site.register(Entry)
