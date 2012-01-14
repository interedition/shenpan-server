from django.core.urlresolvers import reverse
from djangorestframework.resources import ModelResource
from annotatey.api.models import Description, Token,\
    RegularisationType, Scope, Regularisation

class DescriptionResource(ModelResource):
    """A user added description."""
    model = Description

class TokenResource(ModelResource):
    """A user added description."""
    model = Token
    def descriptions(self, instance):
        return instance.descriptions.values_list('text', flat=True)

class RegularisationTypeResource(ModelResource):
    """A user added description."""
    model = RegularisationType
    def descriptions(self, instance):
        return instance.descriptions.values_list('text', flat=True)

class ScopeResource(ModelResource):
    """A user added description."""
    model = Scope
    def descriptions(self, instance):
        return instance.descriptions.values_list('text', flat=True)

class RegularisationResource(ModelResource):
    """A user added description."""
    model = Regularisation
    def descriptions(self, instance):
        return instance.descriptions.values_list('text', flat=True)

