from django.contrib import admin
from .models import JobPosting, Candidate, Application

admin.site.register(JobPosting)
admin.site.register(Candidate)
admin.site.register(Application)