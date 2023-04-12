from django.contrib import admin
from .models import Students,Branch,Subjects,Branch_Subjects,Marks

admin.site.register(Students)
admin.site.register(Branch)
admin.site.register(Subjects)
admin.site.register(Branch_Subjects)
admin.site.register(Marks)
