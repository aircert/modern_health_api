# api/urls.py

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateProgramView, DetailsProgramView, CreateWeekView, DetailsWeekView, CreatePageView, DetailsPageView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = {
	url(r'^auth/', include('rest_framework.urls',
     	namespace='rest_framework')), 
    url(r'^programs/$', CreateProgramView.as_view(), name="createProgram"),
    url(r'^programs/(?P<pk>\d+)$',
        DetailsProgramView.as_view(), name="detailsProgram"),
    url(r'^weeks/$', CreateWeekView.as_view(), name="createWeek"),
    url(r'^weeks/(?P<pk>\d+)$',
        DetailsWeekView.as_view(), name="detailsWeek"),
    url(r'^pages/$', CreatePageView.as_view(), name="createPage"),
    url(r'^pages/(?P<pk>\d+)$',
        DetailsPageView.as_view(), name="detailsPage"),
    url(r'^get-token/', obtain_auth_token)
}

urlpatterns = format_suffix_patterns(urlpatterns)