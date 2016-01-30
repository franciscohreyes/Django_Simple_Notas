from django.conf.urls import include, url
from django.contrib import admin
from Notas.views import ListStatusView, CreateNewEstatusView
import Notas


urlpatterns = [
    url(r'^ListStatus/$', ListStatusView.as_view(), name="ListSsstatus"),
    url(r'^CreateNewStatus/$', CreateNewEstatusView.as_view(), name="NewStatus"),
]

