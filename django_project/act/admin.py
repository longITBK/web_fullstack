from django.contrib import admin
from act.models import Student, Uni, Building, Room, Pizza, Topping, Group, Membership, Person

class StudentsAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]

# Register your models here.
admin.site.register(Building)
admin.site.register(Room)
admin.site.register(Student)
admin.site.register(Uni)
admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Group)
admin.site.register(Membership)
admin.site.register(Person)
