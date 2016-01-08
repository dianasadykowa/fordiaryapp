from django.contrib import admin

from diary.models import Author
from diary.models import Day

admin.site.register(Author)
admin.site.register(Day)

# Register your models here.
