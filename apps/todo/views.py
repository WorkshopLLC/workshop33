from django.shortcuts import render
from django.views.generic import TemplateView

from apps.todo.models import Todo


class TodoHomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(TodoHomeView, self).get_context_data(**kwargs)
        todo_all = Todo.objects.all()
        context['todo_all'] = todo_all
        return context
