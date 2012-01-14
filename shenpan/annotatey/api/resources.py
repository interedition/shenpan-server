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

class RegularisationTypeResource(ModelResource):
    """A user added description."""
    model = RegularisationType
    def descriptions(self):
        return instance.descriptions.values_list('text', flat=True)

class ScopeResource(ModelResource):
    """A user added description."""
    model = Scope

class RegularisationResource(ModelResource):
    """A user added description."""
    model = Regularisation


