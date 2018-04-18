from django.shortcuts import render
from django.views.generic import TemplateView

from apps.todo.models import Todo


class TodoHomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(TodoHomeView, self).get_context_data(**kwargs)
        todo_all = Todo.objects.filter(status='TDO')
        todo_doing_all = Todo.objects.filter(status='DNG')
        todo_done_all = Todo.objects.filter(status='DNE')
        context['todo_all'] = todo_all
        context['todo_doing_all'] = todo_doing_all
        context['todo_done_all'] = todo_done_all
        return context
