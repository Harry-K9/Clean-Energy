from django.conf.urls import url
from django.contrib import admin
from . import Submit
urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^$", Submit.button),
    url(r"output", Submit.output,name="script"),
    url(r"external",Submit.external)
]