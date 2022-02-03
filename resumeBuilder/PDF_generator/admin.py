from django.contrib import admin
from .models import Experience, PersonalInfo, Education, Skills, Projects, About, Awards, resume

# Register your models here.
admin.site.register(Experience)
admin.site.register(PersonalInfo)
admin.site.register(Education)
admin.site.register(Skills)
admin.site.register(Projects)
admin.site.register(About)
admin.site.register(Awards)
admin.site.register(resume)