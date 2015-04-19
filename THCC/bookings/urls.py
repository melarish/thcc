from django.conf.urls import *
#from django.views.generic.simple import *
from views import *
# Enable admin
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^list$', booking_list, name='booking_list'),
    url(r'^booking/(?P<pk>[0-9]+)$', booking_detail, name='booking_detail'),
    url(r'^add$', booking_add, name='booking_add'),
    url(r'^calendar$', booking_calendar, name='booking_calendar'),
    url(r'^submit$', booking_submit, name='booking_submit'),
    url(r'^approve$', booking_approvals, name='booking_approvals'),
    url(r'^mine$', booking_mine, name='booking_mine'),
)
