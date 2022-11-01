from django.contrib import admin
from . models import Review
# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    fieldsets = [
        ('USER INFO', {'fields':['first_name', 'last_name']}),
        ('STARS', {'fields':['stars']})
    ]

admin.site.register(Review, ReviewAdmin)