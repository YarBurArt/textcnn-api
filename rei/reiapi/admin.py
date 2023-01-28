from django.contrib import admin
from .models import Question

# register model for admin page
admin.site.register(Question)
