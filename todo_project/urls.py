from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(('apps.todo.urls', 'apps.todo'), namespace='todo'))
]