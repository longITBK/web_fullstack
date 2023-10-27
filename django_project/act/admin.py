from django.contrib import admin
from act.models import *

class StudentsAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]

# Register your models here.
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)
