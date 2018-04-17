from django.conf.urls import url

from apps.todo.views import TodoHomeView

urlpatterns = [
    url(r'^$', TodoHomeView.as_view(), name='home')
]
