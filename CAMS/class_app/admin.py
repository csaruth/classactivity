from django.contrib import admin

from .models import semester
from .models import Course
from .models import note, submit
from .models import Assignment, submit
from .models import project, submit
from .models import sign_up

#Register your models here.


admin.site.register(semester)
admin.site.register(Course)
admin.site.register(submit)
admin.site.register(note)
admin.site.register(Assignment)
admin.site.register(project)
admin.site.register(sign_up)

