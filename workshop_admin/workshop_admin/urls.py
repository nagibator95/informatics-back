from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    url(r'^admin/', admin.site.urls),
]
