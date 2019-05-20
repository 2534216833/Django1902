from django.contrib import admin
from .models import VoteContent,Vote

# Register your models here.
admin.site.register(VoteContent)
admin.site.register(Vote)