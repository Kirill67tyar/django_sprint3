from django.contrib import admin

from blog.models import (
    Category,
    Post,
    Location,
)


admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Post)
