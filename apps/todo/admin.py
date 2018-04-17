from django.contrib import admin

from apps.todo.models import Todo


class TodoAdmin(admin.ModelAdmin):
    model = Todo


admin.site.register(Todo, TodoAdmin)
