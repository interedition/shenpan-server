"""Urls for the backend."""

from django.conf.urls.defaults import patterns, include, url
from djangorestframework import permissions
from djangorestframework.views import ListOrCreateModelView, InstanceModelView
from regula.backend.resources import DescriptionResource, \
    TokenResource, RegularisationTypeResource, ScopeResource, \
    RegularisationResource


urlpatterns = patterns(
    '',
    url(r'^description/(?P<pk>[0-9]+)/$', \
            InstanceModelView.as_view(
                resource=DescriptionResource,
                permissions=(permissions.IsAuthenticated,)),
        ),
    url(r'^description/$', \
            ListOrCreateModelView.as_view(
                resource=DescriptionResource,
                permissions=(permissions.IsUserOrIsAnonReadOnly,)),
        ),

    url(r'^token/(?P<pk>[0-9]+)/$', \
            InstanceModelView.as_view(
                resource=TokenResource,
                permissions=(permissions.IsAuthenticated,)),
        ),
    url(r'^token/$', \
            ListOrCreateModelView.as_view(
                resource=TokenResource,
                permissions=(permissions.IsUserOrIsAnonReadOnly,)),
        ),

    url(r'^regularisationtype/(?P<pk>[0-9]+)/$', \
            InstanceModelView.as_view(
                resource=RegularisationTypeResource,
                permissions=(permissions.IsAuthenticated,)),
        ),
    url(r'^regularisationtype/$', \
            ListOrCreateModelView.as_view(
                resource=RegularisationTypeResource,
                permissions=(permissions.IsUserOrIsAnonReadOnly,)),
        ),

    url(r'^scope/(?P<pk>[0-9]+)/$', \
            InstanceModelView.as_view(
                resource=ScopeResource,
                permissions=(permissions.IsAuthenticated,)),
        ),
    url(r'^scope/$', \
            ListOrCreateModelView.as_view(
                resource=ScopeResource,
                permissions=(permissions.IsUserOrIsAnonReadOnly,)),
        ),

    url(r'^regularisation/(?P<pk>[0-9]+)/$', \
            InstanceModelView.as_view(
                resource=RegularisationResource,
                permissions=(permissions.IsAuthenticated,)),
        ),
    url(r'^regularisation/$', \
            ListOrCreateModelView.as_view(
                resource=RegularisationResource,
                permissions=(permissions.IsUserOrIsAnonReadOnly,)),
        ),


)
