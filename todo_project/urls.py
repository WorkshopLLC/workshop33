from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

admin.site.site_header = settings.ADMIN_SITE_HEADER

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include(('apps.todo.urls', 'apps.todo'), namespace='todo'))
]
